from chalice import Chalice, Response
import json
import os
import swaggyjenkins
from swaggyjenkins.rest import ApiException

app = Chalice(app_name='jenkins-apiai-webhooks')
app.debug = True

jenkins_ra = swaggyjenkins.RemoteAccessApi()
jenkins_ra.api_client.configuration.host = os.environ.get('jenkins_host')
jenkins_ra.api_client.configuration.username = os.environ.get('jenkins_username')
jenkins_ra.api_client.configuration.password = os.environ.get('jenkins_password')

print 'Using Jenkins instance at: {}, as user: {}'.format(jenkins_ra.api_client.configuration.host, jenkins_ra.api_client.configuration.username)

@app.route('/', methods=['POST'])
def index():

    try:

      print 'Retrieving Jenkins crumb...'
      data, status_code, headers = jenkins_ra.get_crumb_with_http_info()
      print 'Response status code: {}'.format(status_code)
      print 'Using Jenkins crumb: {}'.format(data.crumb)

      opts = {
        'token': 'jenkins-apiai-webhooks',
        'jenkins_crumb': data.crumb
      }
      request_body = app.current_request.json_body
      job_name = request_body['result']['parameters']['job-name'];
      print 'Calling job: {}...'.format(job_name)
      data, status_code, headers = jenkins_ra.post_job_build_with_http_info(job_name, '{}', **opts)
      print 'Response status code: {}'.format(status_code)

      success_speeches = {
        'Brew Coffee': 'Starting the coffee maker...',
        'Call Lady Gaga': 'Calling Lady Gaga...',
        'Dim Light': 'Dimming the light...',
        'Feed The Cat': 'Sending instruction to cat feeder...',
        'Vacuum Living Room': 'Starting the Roomba in the living room...',
        'Wash Dishes': 'Starting the dishwasher...'
      }
      print success_speeches[job_name]
      result = {
        'speech': success_speeches[job_name],
        'displayText': success_speeches[job_name],
        'data': {},
        'contextOut': [],
        'source': 'Jenkins'
      }
      return Response(body=json.dumps(result),
                      status_code=200,
                      headers={'Content-Type': 'application/json'})
    except ApiException, e:
      print 'An error occured: {}'.format(e.reason)
      result = {
        'speech': e.reason,
        'displayText': e.reason + e.body,
        'data': {},
        'contextOut': [],
        'source': 'Jenkins'
      }
      return Response(body=json.dumps(result),
                      status_code=e.status,
                      headers={'Content-Type': 'application/json'})
