import os, shutil

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


# src = "oGG_011"
# src = "oGG_012"
# src = "oGG_014"
# src = "oGG_015"
# src = "oGG_017"
# src = "oGG_018"
# src = "oGG_021"
# src = "oGG_029"
# src = "oGG_032"
# src = "oGG_033"
# src = "oGG_034"
# src = "oGG_035"
# src = "oGG_041"
# src = "oGG_042"
# src = "oGG_043"
# src = "oGG_044"
# src = "oGG_045"
# src = "oGG_053"
# src = "oGG_087"
# src = "oGG_115"
# src = "oGG_136"
# src = "oGG_212"
# src = "oGG_219"

# src = "oGG_001"
# src = "oGG_002"
# src = "oGG_003"
# src = "oGG_004"
# src = "oGG_005"
# src = "oGG_006"
# src = "oGG_007"
# src = "oGG_008"
# src = "oGG_009"
# src = "oGG_010"
# src = "oGG_011"
# src = "oGG_012"
# src = "oGG_013"
# src = "oGG_014"
# src = "oGG_015"
# src = "oGG_016"
# src = "oGG_017"
# src = "oGG_018"
# src = "oGG_019"
# src = "oGG_020"
# src = "oGG_021"
# src = "oGG_022"
# src = "oGG_023"
# src = "oGG_024"
# src = "oGG_025"
# src = "oGG_026"
# src = "oGG_027"
# src = "oGG_028"
# src = "oGG_029"
# src = "oGG_030"
# src = "oGG_031"
# src = "oGG_032"
# src = "oGG_033"
# src = "oGG_034"
# src = "oGG_035"
# src = "oGG_036"
# src = "oGG_037"
# src = "oGG_038"
# src = "oGG_039"
# src = "oGG_040"
# src = "oGG_041"
# src = "oGG_042"
# src = "oGG_043"
# src = "oGG_044"
# src = "oGG_045"
# src = "oGG_046"
# src = "oGG_047"
# src = "oGG_048"
# src = "oGG_049"
# src = "oGG_050"
# src = "oGG_051"
# src = "oGG_052"
# src = "oGG_053"
# src = "oGG_054"
# src = "oGG_055"
# src = "oGG_056"
# src = "oGG_057"
# src = "oGG_058"
# src = "oGG_059"
# src = "oGG_060"
# src = "oGG_061"
# src = "oGG_062"
# src = "oGG_063"
# src = "oGG_064"
# src = "oGG_065"
# src = "oGG_066"
# src = "oGG_067"
# src = "oGG_068"
# src = "oGG_069"
# src = "oGG_070"
# src = "oGG_071"
# src = "oGG_072"
# src = "oGG_073"
# src = "oGG_074"
# src = "oGG_075"
# src = "oGG_076"
# src = "oGG_077"
# src = "oGG_078"
# src = "oGG_079"
# src = "oGG_080"
# src = "oGG_081"
# src = "oGG_082"
# src = "oGG_083"
# src = "oGG_084"
# src = "oGG_085"
# src = "oGG_086"
# src = "oGG_087"
# src = "oGG_088"
# src = "oGG_089"
# src = "oGG_090"
# src = "oGG_091"
# src = "oGG_092"
# src = "oGG_093"
# src = "oGG_094"
# src = "oGG_095"
# src = "oGG_096"
# src = "oGG_097"
# src = "oGG_098"
# src = "oGG_099"
# src = "oGG_100"
# src = "oGG_101"
# src = "oGG_102"
# src = "oGG_103"
# src = "oGG_104"
# src = "oGG_105"
# src = "oGG_106"
# src = "oGG_107"
# src = "oGG_108"
# src = "oGG_109"
# src = "oGG_110"
# src = "oGG_111"
# src = "oGG_112"
# src = "oGG_113"
# src = "oGG_114"
# src = "oGG_115"
# src = "oGG_116"
# src = "oGG_117"
# src = "oGG_118"
# src = "oGG_119"
# src = "oGG_120"
# src = "oGG_121"
# src = "oGG_122"
# src = "oGG_123"
# src = "oGG_124"
# src = "oGG_125"
# src = "oGG_126"
# src = "oGG_127"
# src = "oGG_128"
# src = "oGG_129"
# src = "oGG_130"
# src = "oGG_131"
# src = "oGG_132"
# src = "oGG_133"
# src = "oGG_134"
# src = "oGG_135"
# src = "oGG_136"
# src = "oGG_137"
# src = "oGG_138"
# src = "oGG_139"
# src = "oGG_140"
# src = "oGG_141"
# src = "oGG_142"
# src = "oGG_143"
# src = "oGG_144"
# src = "oGG_145"
# src = "oGG_146"
# src = "oGG_147"
# src = "oGG_148"
# src = "oGG_149"
# src = "oGG_150"
# src = "oGG_151"
# src = "oGG_152"
# src = "oGG_153"
# src = "oGG_154"
# src = "oGG_155"
# src = "oGG_156"
# src = "oGG_157"
# src = "oGG_158"
# src = "oGG_159"
# src = "oGG_160"
# src = "oGG_161"
# src = "oGG_162"
# src = "oGG_163"
# src = "oGG_164"
# src = "oGG_165"
# src = "oGG_166"
# src = "oGG_167"
# src = "oGG_168"
# src = "oGG_169"
# src = "oGG_170"
# src = "oGG_171"
# src = "oGG_172"
# src = "oGG_173"
# src = "oGG_174"
# src = "oGG_175"
# src = "oGG_176"
# src = "oGG_177"
# src = "oGG_178"
# src = "oGG_179"
# src = "oGG_180"
# src = "oGG_181"
# src = "oGG_182"
# src = "oGG_183"
# src = "oGG_184"
# src = "oGG_185"
# src = "oGG_186"
# src = "oGG_187"
# src = "oGG_188"
# src = "oGG_189"
# src = "oGG_190"
# src = "oGG_191"
# src = "oGG_192"
# src = "oGG_193"
# src = "oGG_194"
# src = "oGG_195"
# src = "oGG_196"
# src = "oGG_197"
# src = "oGG_198"
# src = "oGG_199"
# src = "oGG_200"
# src = "oGG_201"
# src = "oGG_202"
# src = "oGG_203"
# src = "oGG_204"
# src = "oGG_205"
# src = "oGG_206"
# src = "oGG_207"
# src = "oGG_208"
# src = "oGG_209"
# src = "oGG_210"
# src = "oGG_211"
# src = "oGG_212"
# src = "oGG_213"
# src = "oGG_214"
# src = "oGG_215"
# src = "oGG_216"
# src = "oGG_217"
# src = "oGG_218"
# src = "oGG_219"


# dst = "gundepy/GGBOOK-oGG_001"
# dst = "gundepy/GGBOOK-oGG_002"
# dst = "gundepy/GGBOOK-oGG_003"
# dst = "gundepy/GGBOOK-oGG_004"
# dst = "gundepy/GGBOOK-oGG_005"
# dst = "gundepy/GGBOOK-oGG_006"
# dst = "gundepy/GGBOOK-oGG_007"
# dst = "gundepy/GGBOOK-oGG_008"
# dst = "gundepy/GGBOOK-oGG_009"
# dst = "gundepy/GGBOOK-oGG_010"
# dst = "gundepy/GGBOOK-oGG_011"
# dst = "gundepy/GGBOOK-oGG_012"
# dst = "gundepy/GGBOOK-oGG_013"
# dst = "gundepy/GGBOOK-oGG_014"
# dst = "gundepy/GGBOOK-oGG_015"
# dst = "gundepy/GGBOOK-oGG_016"
# dst = "gundepy/GGBOOK-oGG_017"
# dst = "gundepy/GGBOOK-oGG_018"
# dst = "gundepy/GGBOOK-oGG_019"
# dst = "gundepy/GGBOOK-oGG_020"
# dst = "gundepy/GGBOOK-oGG_021"
# dst = "gundepy/GGBOOK-oGG_022"
# dst = "gundepy/GGBOOK-oGG_023"
# dst = "gundepy/GGBOOK-oGG_024"
# dst = "gundepy/GGBOOK-oGG_025"
# dst = "gundepy/GGBOOK-oGG_026"
# dst = "gundepy/GGBOOK-oGG_027"
# dst = "gundepy/GGBOOK-oGG_028"
# dst = "gundepy/GGBOOK-oGG_029"
# dst = "gundepy/GGBOOK-oGG_030"
# dst = "gundepy/GGBOOK-oGG_031"
# dst = "gundepy/GGBOOK-oGG_032"
# dst = "gundepy/GGBOOK-oGG_033"
# dst = "gundepy/GGBOOK-oGG_034"
# dst = "gundepy/GGBOOK-oGG_035"
# dst = "gundepy/GGBOOK-oGG_036"
# dst = "gundepy/GGBOOK-oGG_037"
# dst = "gundepy/GGBOOK-oGG_038"
# dst = "gundepy/GGBOOK-oGG_039"
# dst = "gundepy/GGBOOK-oGG_040"
# dst = "gundepy/GGBOOK-oGG_041"
# dst = "gundepy/GGBOOK-oGG_042"
# dst = "gundepy/GGBOOK-oGG_043"
# dst = "gundepy/GGBOOK-oGG_044"
# dst = "gundepy/GGBOOK-oGG_045"
# dst = "gundepy/GGBOOK-oGG_046"
# dst = "gundepy/GGBOOK-oGG_047"
# dst = "gundepy/GGBOOK-oGG_048"
# dst = "gundepy/GGBOOK-oGG_049"
# dst = "gundepy/GGBOOK-oGG_050"
# dst = "gundepy/GGBOOK-oGG_051"
# dst = "gundepy/GGBOOK-oGG_052"
# dst = "gundepy/GGBOOK-oGG_053"
# dst = "gundepy/GGBOOK-oGG_054"
# dst = "gundepy/GGBOOK-oGG_055"
# dst = "gundepy/GGBOOK-oGG_056"
# dst = "gundepy/GGBOOK-oGG_057"
# dst = "gundepy/GGBOOK-oGG_058"
# dst = "gundepy/GGBOOK-oGG_059"
# dst = "gundepy/GGBOOK-oGG_060"
# dst = "gundepy/GGBOOK-oGG_061"
# dst = "gundepy/GGBOOK-oGG_062"
# dst = "gundepy/GGBOOK-oGG_063"
# dst = "gundepy/GGBOOK-oGG_064"
# dst = "gundepy/GGBOOK-oGG_065"
# dst = "gundepy/GGBOOK-oGG_066"
# dst = "gundepy/GGBOOK-oGG_067"
# dst = "gundepy/GGBOOK-oGG_068"
# dst = "gundepy/GGBOOK-oGG_069"
# dst = "gundepy/GGBOOK-oGG_070"
# dst = "gundepy/GGBOOK-oGG_071"
# dst = "gundepy/GGBOOK-oGG_072"
# dst = "gundepy/GGBOOK-oGG_073"
# dst = "gundepy/GGBOOK-oGG_074"
# dst = "gundepy/GGBOOK-oGG_075"
# dst = "gundepy/GGBOOK-oGG_076"
# dst = "gundepy/GGBOOK-oGG_077"
# dst = "gundepy/GGBOOK-oGG_078"
# dst = "gundepy/GGBOOK-oGG_079"
# dst = "gundepy/GGBOOK-oGG_080"
# dst = "gundepy/GGBOOK-oGG_081"
# dst = "gundepy/GGBOOK-oGG_082"
# dst = "gundepy/GGBOOK-oGG_083"
# dst = "gundepy/GGBOOK-oGG_084"
# dst = "gundepy/GGBOOK-oGG_085"
# dst = "gundepy/GGBOOK-oGG_086"
# dst = "gundepy/GGBOOK-oGG_087"
# dst = "gundepy/GGBOOK-oGG_088"
# dst = "gundepy/GGBOOK-oGG_089"
# dst = "gundepy/GGBOOK-oGG_090"
# dst = "gundepy/GGBOOK-oGG_091"
# dst = "gundepy/GGBOOK-oGG_092"
# dst = "gundepy/GGBOOK-oGG_093"
# dst = "gundepy/GGBOOK-oGG_094"
# dst = "gundepy/GGBOOK-oGG_095"
# dst = "gundepy/GGBOOK-oGG_096"
# dst = "gundepy/GGBOOK-oGG_097"
# dst = "gundepy/GGBOOK-oGG_098"
# dst = "gundepy/GGBOOK-oGG_099"
# dst = "gundepy/GGBOOK-oGG_100"
# dst = "gundepy/GGBOOK-oGG_101"
# dst = "gundepy/GGBOOK-oGG_102"
# dst = "gundepy/GGBOOK-oGG_103"
# dst = "gundepy/GGBOOK-oGG_104"
# dst = "gundepy/GGBOOK-oGG_105"
# dst = "gundepy/GGBOOK-oGG_106"
# dst = "gundepy/GGBOOK-oGG_107"
# dst = "gundepy/GGBOOK-oGG_108"
# dst = "gundepy/GGBOOK-oGG_109"
# dst = "gundepy/GGBOOK-oGG_110"
# dst = "gundepy/GGBOOK-oGG_111"
# dst = "gundepy/GGBOOK-oGG_112"
# dst = "gundepy/GGBOOK-oGG_113"
# dst = "gundepy/GGBOOK-oGG_114"
# dst = "gundepy/GGBOOK-oGG_115"
# dst = "gundepy/GGBOOK-oGG_116"
# dst = "gundepy/GGBOOK-oGG_117"
# dst = "gundepy/GGBOOK-oGG_118"
# dst = "gundepy/GGBOOK-oGG_119"
# dst = "gundepy/GGBOOK-oGG_120"
# dst = "gundepy/GGBOOK-oGG_121"
# dst = "gundepy/GGBOOK-oGG_122"
# dst = "gundepy/GGBOOK-oGG_123"
# dst = "gundepy/GGBOOK-oGG_124"
# dst = "gundepy/GGBOOK-oGG_125"
# dst = "gundepy/GGBOOK-oGG_126"
# dst = "gundepy/GGBOOK-oGG_127"
# dst = "gundepy/GGBOOK-oGG_128"
# dst = "gundepy/GGBOOK-oGG_129"
# dst = "gundepy/GGBOOK-oGG_130"
# dst = "gundepy/GGBOOK-oGG_131"
# dst = "gundepy/GGBOOK-oGG_132"
# dst = "gundepy/GGBOOK-oGG_133"
# dst = "gundepy/GGBOOK-oGG_134"
# dst = "gundepy/GGBOOK-oGG_135"
# dst = "gundepy/GGBOOK-oGG_136"
# dst = "gundepy/GGBOOK-oGG_137"
# dst = "gundepy/GGBOOK-oGG_138"
# dst = "gundepy/GGBOOK-oGG_139"
# dst = "gundepy/GGBOOK-oGG_140"
# dst = "gundepy/GGBOOK-oGG_141"
# dst = "gundepy/GGBOOK-oGG_142"
# dst = "gundepy/GGBOOK-oGG_143"
# dst = "gundepy/GGBOOK-oGG_144"
# dst = "gundepy/GGBOOK-oGG_145"
# dst = "gundepy/GGBOOK-oGG_146"
# dst = "gundepy/GGBOOK-oGG_147"
# dst = "gundepy/GGBOOK-oGG_148"
# dst = "gundepy/GGBOOK-oGG_149"
# dst = "gundepy/GGBOOK-oGG_150"
# dst = "gundepy/GGBOOK-oGG_151"
# dst = "gundepy/GGBOOK-oGG_152"
# dst = "gundepy/GGBOOK-oGG_153"
# dst = "gundepy/GGBOOK-oGG_154"
# dst = "gundepy/GGBOOK-oGG_155"
# dst = "gundepy/GGBOOK-oGG_156"
# dst = "gundepy/GGBOOK-oGG_157"
# dst = "gundepy/GGBOOK-oGG_158"
# dst = "gundepy/GGBOOK-oGG_159"
# dst = "gundepy/GGBOOK-oGG_160"
# dst = "gundepy/GGBOOK-oGG_161"
# dst = "gundepy/GGBOOK-oGG_162"
# dst = "gundepy/GGBOOK-oGG_163"
# dst = "gundepy/GGBOOK-oGG_164"
# dst = "gundepy/GGBOOK-oGG_165"
# dst = "gundepy/GGBOOK-oGG_166"
# dst = "gundepy/GGBOOK-oGG_167"
# dst = "gundepy/GGBOOK-oGG_168"
# dst = "gundepy/GGBOOK-oGG_169"
# dst = "gundepy/GGBOOK-oGG_170"
# dst = "gundepy/GGBOOK-oGG_171"
# dst = "gundepy/GGBOOK-oGG_172"
# dst = "gundepy/GGBOOK-oGG_173"
# dst = "gundepy/GGBOOK-oGG_174"
# dst = "gundepy/GGBOOK-oGG_175"
# dst = "gundepy/GGBOOK-oGG_176"
# dst = "gundepy/GGBOOK-oGG_177"
# dst = "gundepy/GGBOOK-oGG_178"
# dst = "gundepy/GGBOOK-oGG_179"
# dst = "gundepy/GGBOOK-oGG_180"
# dst = "gundepy/GGBOOK-oGG_181"
# dst = "gundepy/GGBOOK-oGG_182"
# dst = "gundepy/GGBOOK-oGG_183"
# dst = "gundepy/GGBOOK-oGG_184"
# dst = "gundepy/GGBOOK-oGG_185"
# dst = "gundepy/GGBOOK-oGG_186"
# dst = "gundepy/GGBOOK-oGG_187"
# dst = "gundepy/GGBOOK-oGG_188"
# dst = "gundepy/GGBOOK-oGG_189"
# dst = "gundepy/GGBOOK-oGG_190"
# dst = "gundepy/GGBOOK-oGG_191"
# dst = "gundepy/GGBOOK-oGG_192"
# dst = "gundepy/GGBOOK-oGG_193"
# dst = "gundepy/GGBOOK-oGG_194"
# dst = "gundepy/GGBOOK-oGG_195"
# dst = "gundepy/GGBOOK-oGG_196"
# dst = "gundepy/GGBOOK-oGG_197"
# dst = "gundepy/GGBOOK-oGG_198"
# dst = "gundepy/GGBOOK-oGG_199"
# dst = "gundepy/GGBOOK-oGG_200"
# dst = "gundepy/GGBOOK-oGG_201"
# dst = "gundepy/GGBOOK-oGG_202"
# dst = "gundepy/GGBOOK-oGG_203"
# dst = "gundepy/GGBOOK-oGG_204"
# dst = "gundepy/GGBOOK-oGG_205"
# dst = "gundepy/GGBOOK-oGG_206"
# dst = "gundepy/GGBOOK-oGG_207"
# dst = "gundepy/GGBOOK-oGG_208"
# dst = "gundepy/GGBOOK-oGG_209"
# dst = "gundepy/GGBOOK-oGG_210"
# dst = "gundepy/GGBOOK-oGG_211"
# dst = "gundepy/GGBOOK-oGG_212"
# dst = "gundepy/GGBOOK-oGG_213"
# dst = "gundepy/GGBOOK-oGG_214"
# dst = "gundepy/GGBOOK-oGG_215"
# dst = "gundepy/GGBOOK-oGG_216"
# dst = "gundepy/GGBOOK-oGG_217"
# dst = "gundepy/GGBOOK-oGG_218"
# dst = "gundepy/GGBOOK-oGG_219"


copytree(src, dst)


# os.listdir (just the list), copytree (copies tree folder structure), shutil copy (copies files)
# os.path.exists will also return True if there's a regular file with that name.
# os.path.isdir will only return True if that path exists and is a directory.
#finally figured it out by adding another if path exists sweetfoldername.  yay!