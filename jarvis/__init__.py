import os
import argparse
import traceback

ml = None

# This is the place where is stored the currently tested 'module.function' .
TEST_MODULE_PATH="testmodule.txt"

# This is the file where errors produced by calls to jarvis.command.error are written.
ERROR_FILE="error.txt"
DEBUG_FILE="debug.txt"

def get_home():
    jarvis_home = os.getenv("JARVIS_HOME", "/tmp/jarvis")
    try:
        os.makedirs(jarvis_home)
    except OSError, e:
        if e.errno != 17:
            raise
        
    return jarvis_home

def get_filename(key):
    error_file = os.path.join(get_home(), key)    
    return error_file

def run(modulename, layout=None):
    global ml
    import qtdisplay
    import mainloop

    try:
        ml = mainloop.MainLoop(modulename)
        
        display = qtdisplay.QTDisplay(ml, layout)
        ml.setdisplay(display)

        display.init()
        
    except KeyboardInterrupt:
        pass
    except Exception, e:
        print traceback.format_exc(e)
    finally:
        display.destroy()
        

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("--nogl", default=False, action="store_true", help="disable gl window")
    parser.add_argument("--module", metavar="NAME")
    parser.add_argument("--layout", metavar="LAYOUT", default=None)

    args = parser.parse_args()
    run(args.module, args.layout)

def debug(*args):
    global ml
    if ml != None and ml.display != None:
        ml.display.debugprint(*args)

def error(*args):
    print "ERROR PRINT", args
    global ml
    if ml != None and ml.display != None:
        ml.display.errorprint(*args)
    
def debug_dir(object, filt = None):
    debug("debug_dir", object, filt)   
    for k in dir(object):        
        if filt == None or filt in k.lower():
            debug(k)    

def debug_xml(*args):
    debug(*(list(args[:-1]) + [etree.tostring(args[-1], pretty_print = True)]))

def testunit_result(result):
    for err in result.errors:
        error(err[1])

def show(osgdata):
    global ml
    if ml != None and ml.display != None:
        ml.display.osgprint(osgdata)
    
def get_osg_viewer():
    global ml
    if ml != None and ml.display != None:
        return ml.display.getosgviewer()

def setlooptime(loop_time):
    global ml
    if ml != None and ml.display != None:
        ml.display.setlooptime(loop_time)

>>>>>>> 4b6d3b03ae8b38fc7851e88be0ec3c0d3e270dfe

if __name__ == "__main__":
    main()

