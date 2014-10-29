import sys, os, shutil

src = str(sys.argv[1])
dst = str(sys.argv[2])

def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        # print s, d
        # print "JOIN", os.path.join(d, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            # os.makedirs(os.path.join(d, item))
            if not os.path.exists(d) or os.stat(src).st_mtime - os.stat(dst).st_mtime > 1:
                sweetfoldername = os.path.splitext(d)[0]
                if not os.path.exists(sweetfoldername):
                    os.mkdir(sweetfoldername)
                if d.endswith(".tif"):
                    shutil.copy2(s, sweetfoldername)
                    # print "jpg", os.path.splitext(d)[0]
                elif d.endswith(".xml"):
                    shutil.copy2(s, sweetfoldername) #if there's just xml and no matching it takes out the extension
                else:
                    print "NOT FOR INGEST", d



copytree(src, dst)


# os.listdir (just the list), copytree (copies tree folder structure), shutil copy (copies files)
# os.path.exists will also return True if there's a regular file with that name.
# os.path.isdir will only return True if that path exists and is a directory.
#finally figured it out by adding another if path exists sweetfoldername.  yay!

# updated bookbatch to use from the command line.  use this script in the command line:  python bookbatch2.py oGG_003-sys.argv[1] gundepy/GGBOOK-oGG_003-sys.argv[2]

#to try and do it recursively, and to make a new folder
# for num in {1..1000}; do for dir in /Users/dsuuser/Desktop/kim/gunde/STEP1-DONEimagemagick/hey2/*; do (mkdir /Users/dsuuser/Desktop/kim/gunde/STEP1-DONEimagemagick/gundepy/$num && python /Users/dsuuser/Desktop/kim/gunde/STEP1-DONEimagemagick/bookbatch2.py $dir /Users/dsuuser/Desktop/kim/gunde/STEP1-DONEimagemagick/gundepy/$dir); done


# for dir in /Users/dsuuser/Desktop/kim/gunde/STEP1-DONEimagemagick/hey2/*; do python /Users/dsuuser/Desktop/kim/gunde/STEP1-DONEimagemagick/bookbatch2.py $dir /Users/dsuuser/Desktop/kim/gunde/STEP1-DONEimagemagick/gundepy/{A..Z}; done


#trying to rename all images to OBJ and xml to MODS....still in progress to figure it out
# for f in test/*; find . -iname "*.tif" -exec rename *.tif OBJ.tif '{}' \;