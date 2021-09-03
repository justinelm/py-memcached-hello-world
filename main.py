from pymemcache.client.base import Client

#init redis
m = Client(("cdmp-lab21-jm-2.escwrb.cfg.apse1.cache.amazonaws.com", 11211))
#set keys
m.set('hello', 'world')
#get keys

#return ok
print(m.get('hello')) 