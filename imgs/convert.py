import os

for f in ['f435w','f606w','f775w','f814w','f850lp','f105w','f125w','f140w','f160w']:
    os.system('convert orig/'+f+'.1.sci.inverted.tiff '+f+'.png')