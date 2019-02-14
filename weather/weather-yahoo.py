# Weather API Python sample code
# Copyright 2019 Oath Inc. Licensed under the terms of the zLib license see https://opensource.org/licenses/Zlib for terms.
# $ python --version
# Python 2.7.10

import time, uuid, urllib
import urllib.request, urllib.error, urllib.parse
import hmac, hashlib
from base64 import b64encode

url = 'https://weather-ydn-yql.media.yahoo.com/forecastrss'
method = 'GET'
app_id = 'YP8uZC56'
consumer_key = 'dj0yJmk9MDN5SVNHQUdhTmFMJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTA2'
consumer_secret = '34597fa517001204771ea4d02765a36e89006ba2'
concat = '&'
query = {'location': 'sunnyvale,ca', 'format': 'json'}
oauth = {
    'oauth_consumer_key': consumer_key,
    'oauth_nonce': uuid.uuid4().hex,
    'oauth_signature_method': 'HMAC-SHA1',
    'oauth_timestamp': str(int(time.time())),
    'oauth_version': '1.0'
}

# Prepare signature string (merge all params and SORT them)
merged_params = query.copy()
merged_params.update(oauth)
sorted_params = [k + '=' + urllib.parse.quote(merged_params[k], safe='') for k in sorted(merged_params.keys())]
signature_base_str =  method + concat + urllib.parse.quote(url, safe='') + concat + urllib.parse.quote(concat.join(sorted_params), safe='')

# Generate signature
composite_key = urllib.parse.quote(consumer_secret, safe='') + concat
oauth_signature = b64encode(hmac.new(bytearray(composite_key.upper(), 'utf-8'), bytearray(signature_base_str, 'utf-8'), hashlib.sha1).digest())

# Prepare Authorization header
oauth['oauth_signature'] = oauth_signature
auth_header = 'OAuth ' + ', '.join(['{}="{}"'.format(k,v) for k,v in oauth.items()])

# Send request
url = url + '?' + urllib.parse.urlencode(query)
req = urllib.request.urlopen(url)
req.add_header('Authorization', auth_header)
req.add_header('Yahoo-App-Id', app_id)
response = urllib.request.urlopen(req).read()
print(response)