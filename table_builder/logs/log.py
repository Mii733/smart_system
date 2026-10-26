import functools
import logging
import socket 
import webbrowser
hostname = socket.gethostname() 
IPAddr = socket.gethostbyname(hostname)

logging.basicConfig(
    filename='logs\\logger.log', 
    format='%(asctime)s %(module)s   %(name)s  %(levelname)s: %(message)s',
    level=logging.INFO)

def loggingrecord(request):
    data = list(request.POST.items())[1:]
    logging.info("{0} - {1} {2} ".format(request.user.username +'/'+hostname + '/' + IPAddr +' /' , webbrowser.get().name , data))

