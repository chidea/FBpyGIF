FBIOGET_VSCREENINFO=0x4600
FBIOPUT_VSCREENINFO=0x4601
FBIOGET_FSCREENINFO=0x4602
FBIOGETCMAP=0x4604
FBIOPUTCMAP=0x4605
FBIOPAN_DISPLAY=0x4606

#FBIO_CURSOR            IOWR('F', 0x08, struct fb_cursor)
FBIOGET_CON2FBMAP=0x460F
FBIOPUT_CON2FBMAP=0x4610
FBIOBLANK=0x4611
#FBIOGET_VBLANK=IOR('F',0x12, struct fb_vblank)
FBIO_ALLOC=0x4613
FBIO_FREE=0x4614
FBIOGET_GLYPH=0x4615
FBIOGET_HWCINFO=0x4616
FBIOPUT_MODEINFO=0x4617
FBIOGET_DISPINFO=0x4618
#FBIO_WAITFORVSYNC=IOW('F', 0x20, u32)
FB_TYPE_PACKED_PIXELS=0
FB_TYPE_PLANES=1
FB_TYPE_INTERLEAVED_PLANES=2
FB_TYPE_TEXT=3
FB_TYPE_VGA_PLANES=4
FB_TYPE_FOURCC=5

FB_AUX_TEXT_MDA=0
FB_AUX_TEXT_CGA=1
FB_AUX_TEXT_S3_MMIO=2
FB_AUX_TEXT_MGA_STEP16=3
FB_AUX_TEXT_MGA_STEP8=4
FB_AUX_TEXT_SVGA_GROUP=8
FB_AUX_TEXT_SVGA_MASK=7
FB_AUX_TEXT_SVGA_STEP2=8
FB_AUX_TEXT_SVGA_STEP4=9
FB_AUX_TEXT_SVGA_STEP8=10
FB_AUX_TEXT_SVGA_STEP16=11
FB_AUX_TEXT_SVGA_LAST=15

FB_AUX_VGA_PLANES_VGA4=0
FB_AUX_VGA_PLANES_CFB4=1
FB_AUX_VGA_PLANES_CFB8=2

FB_VISUAL_MONO01=0
FB_VISUAL_MONO10=1
FB_VISUAL_TRUECOLOR=2
FB_VISUAL_PSEUDOCOLOR=3
FB_VISUAL_DIRECTCOLOR=4
FB_VISUAL_STATIC_PSEUDOCOLOR=5
FB_VISUAL_FOURCC=6

FB_ACCEL_NONE=0
FB_ACCEL_ATARIBLITT=1
FB_ACCEL_AMIGABLITT=2
FB_ACCEL_S3_TRIO64=3
FB_ACCEL_NCR_77C32BLT=4
FB_ACCEL_S3_VIRGE=5
FB_ACCEL_ATI_MACH64GX=6
FB_ACCEL_DEC_TGA=7
FB_ACCEL_ATI_MACH64CT=8
FB_ACCEL_ATI_MACH64VT=9
FB_ACCEL_ATI_MACH64GT=10
FB_ACCEL_SUN_CREATOR=11
FB_ACCEL_SUN_CGSIX=12
FB_ACCEL_SUN_LEO=13
FB_ACCEL_IMS_TWINTURBO=14
FB_ACCEL_3DLABS_PERMEDIA2=15
FB_ACCEL_MATROX_MGA2064W=16
FB_ACCEL_MATROX_MGA1064SG=17
FB_ACCEL_MATROX_MGA2164W=18
FB_ACCEL_MATROX_MGA2164W_AGP=19
FB_ACCEL_MATROX_MGAG100=20
FB_ACCEL_MATROX_MGAG200=21
FB_ACCEL_SUN_CG14=22
FB_ACCEL_SUN_BWTWO=23
FB_ACCEL_SUN_CGTHREE=24
FB_ACCEL_SUN_TCX=25
FB_ACCEL_MATROX_MGAG400=26
FB_ACCEL_NV3=27
FB_ACCEL_NV4=28
FB_ACCEL_NV5=29
FB_ACCEL_CT_6555x=30
FB_ACCEL_3DFX_BANSHEE=31
FB_ACCEL_ATI_RAGE128=32
FB_ACCEL_IGS_CYBER2000=33
FB_ACCEL_IGS_CYBER2010=34
FB_ACCEL_IGS_CYBER5000=35
FB_ACCEL_SIS_GLAMOUR=36
FB_ACCEL_3DLABS_PERMEDIA3=37
FB_ACCEL_ATI_RADEON=38
FB_ACCEL_I810=39
FB_ACCEL_SIS_GLAMOUR_2=40
FB_ACCEL_SIS_XABRE=41
FB_ACCEL_I830=42
FB_ACCEL_NV_10=43
FB_ACCEL_NV_20=44
FB_ACCEL_NV_30=45
FB_ACCEL_NV_40=46
FB_ACCEL_XGI_VOLARI_V=47
FB_ACCEL_XGI_VOLARI_Z=48
FB_ACCEL_OMAP1610=49
FB_ACCEL_TRIDENT_TGUI=50
FB_ACCEL_TRIDENT_3DIMAGE=51
FB_ACCEL_TRIDENT_BLADE3D=52
FB_ACCEL_TRIDENT_BLADEXP=53
FB_ACCEL_CIRRUS_ALPINE=53
FB_ACCEL_NEOMAGIC_NM2070=90
FB_ACCEL_NEOMAGIC_NM2090=91
FB_ACCEL_NEOMAGIC_NM2093=92
FB_ACCEL_NEOMAGIC_NM2097=93
FB_ACCEL_NEOMAGIC_NM2160=94
FB_ACCEL_NEOMAGIC_NM2200=95
FB_ACCEL_NEOMAGIC_NM2230=96
FB_ACCEL_NEOMAGIC_NM2360=97
FB_ACCEL_NEOMAGIC_NM2380=98
FB_ACCEL_PXA3XX=99

FB_ACCEL_SAVAGE4=0x80
FB_ACCEL_SAVAGE3D=0x81
FB_ACCEL_SAVAGE3D_MV=0x82
FB_ACCEL_SAVAGE2000=0x83
FB_ACCEL_SAVAGE_MX_MV=0x84
FB_ACCEL_SAVAGE_MX=0x85
FB_ACCEL_SAVAGE_IX_MV=0x86
FB_ACCEL_SAVAGE_IX=0x87
FB_ACCEL_PROSAVAGE_PM=0x88
FB_ACCEL_PROSAVAGE_KM=0x89
FB_ACCEL_S3TWISTER_P=0x8a   
FB_ACCEL_S3TWISTER_K=0x8b   
FB_ACCEL_SUPERSAVAGE=0x8c   
FB_ACCEL_PROSAVAGE_DDR=0x8d 
FB_ACCEL_PROSAVAGE_DDRK=0x8e

FB_ACCEL_PUV3_UNIGFX=0xa0

from PIL.Image import ANTIALIAS

from mmap import mmap
from fcntl import ioctl
import struct

mm = None
bpp, w, h = 0, 0, 0 # framebuffer bpp and size
bytepp = 0
vx, vy, vw, vh = 0, 0, 0, 0 #virtual window offset and size
vi, fi = None, None
_fb_cmap = 'IIPPPP' # start, len, r, g, b, a
RGB = False
_verbose = False
msize_kb = 0

def report_fb(i=0, layer=0):
  with open('/dev/fb'+str(i), 'r+b')as f:
    vi = ioctl(f, FBIOGET_VSCREENINFO, bytes(160))
    vi = list(struct.unpack('I'*40, vi))
    print(vi)
    ffm = 'c'*16+'L'+'I'*4+'H'*3+'ILIIHHH'
    fic = struct.calcsize(ffm)
    fi = struct.unpack(ffm, ioctl(f, FBIOGET_FSCREENINFO, bytes(fic)))
    print(fi)

def ready_fb(_bpp=None, i=0, layer=0, _win=None):
  global mm, bpp, w, h, vi, fi, RGB, msize_kb, vx, vy, vw, vh, bytepp
  if mm and bpp == _bpp: return mm, w, h, bpp
  with open('/dev/fb'+str(i), 'r+b')as f:
    vi = ioctl(f, FBIOGET_VSCREENINFO, bytes(160))
    vi = list(struct.unpack('I'*40, vi))
    #(1920, 1080, 1920, 1080, 0, 0, 24, 0,
    #   w     h     vw    vh  xo yo bpp col 
    #            virtual size offset    1=gray
    # 16, 8, 0, 8, 8, 0, 0, 8, 0, 24, 0, 0, 0, 0, 4294967295, 4294967295, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    #   (bit offset, bits, bigend)         non acv   height(mm) width(mm) accl, pixclock, .....                angle, colorspace, reserved[4]
    #     R        G      B      A        std
    bpp = vi[6]
    bytepp = bpp//8
    if _bpp:
      vi[6] = _bpp # 24 bit = BGR 888 mode
      #vi[8] = 0
      #vi[14] = 16
      try:
        vi = ioctl(f, FBIOPUT_VSCREENINFO, struct.pack('I'*40, *vi)) # fb_var_screeninfo
        vi = struct.unpack('I'*40,vi)
        bpp = vi[6]
        bytepp = bpp//8
      except:
        pass
    
    if vi[8] == 0 : RGB = True
    #r_o, r_b, r_e = vi[8:11]
    #g_o, g_b, g_e = vi[11:14]
    #b_o, b_b, b_e = vi[14:17]
    
    ffm = 'c'*16+'L'+'I'*4+'H'*3+'ILIIHHH'
    fic = struct.calcsize(ffm)
    fi = struct.unpack(ffm, ioctl(f, FBIOGET_FSCREENINFO, bytes(fic)))
    #(b'B', b'C', b'M', b'2', b'7', b'0', b'8', b' ', b'F', b'B', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', 
    # 16 char =id
    # 1025519616, 6220800, 0, 0, 2, 1, 1, 0, 5760, 0, 0, 0, 0, 0, 0)
    # smem_len      type type_aux, visual, xpanstep, ypanstep, ywrapstep, line_length, mmio_start, mmio_len, accel, capabilities, reserved[2]
    msize = fi[17] # = w*h*bpp//8
    ll, start = fi[-7:-5]
    # bpp = vi[9]+vi[12]+vi[15]+vi[18]
    w, h = ll//bytepp, vi[1] # when screen is vertical, width becomes wrong. ll//3 is more accurate at such time.
    if _win and len(_win)==4: # virtual window settings
      vx, vy, vw, vh = _win
      if vw == 'w': vw = w
      if vh == 'h': vh = h
      vx, vy, vw, vh = map(int, (vx, vy, vw, vh))
      if vx>=w: vx = 0
      if vy>=h: vy = 0
      if vx>w: vw = w - vx
      else: vw -= vx
      if vy>h: vh = h - vy
      else: vh -= vy
    else:
      vx, vy, vw, vh = 0,0,w,h
    #msize_kb = w*h*bpp//8//1024 # more accurate FB memory size in kb
    msize_kb = vw*vh*bytepp//1024 # more accurate FB memory size in kb
    #xo, yo = vi[4], vi[5]

    mm = mmap(f.fileno(), msize, offset=start)
    return mm, w, h, bpp#ll//(bpp//8), h

def magick(fpath):
  ''' Use ImageMagick to convert to BGR '''
  from subprocess import check_output, PIPE
  try:
    if b'ImageMagick' not in check_output('convert'):#, stdout=PIPE).stdout:
      return
  except FileNotFoundError:
    return
  p = run(['convert', '-verbose', '-coalesce', '-resize', "%dx%d"%(vw,vh), fpath, ('bgr' if bpp < 32 else 'bgra')+':-'], stdout=PIPE, stderr=PIPE, bufsize=0)
  p, m = p.stdout, p.stderr
  from re import findall
  m = len(findall(b'gif\[([0-9]+)\]', m)) # may hang on single frame files
  if not m : return p
  r=[]
  s=len(p)//m
  for i in range(m):
    r.append(p[s*i:s*(i+1)])
  return r

def fill_scr(r,g,b):
  if bpp == 32:
    seed = struct.pack('BBBB', b, g, r, 255)
  elif bpp == 24:
    seed = struct.pack('BBB', b, g, r)
  elif bpp == 16:
    seed = struct.pack('H', r>>3<<11 | g>>2<<5 | b>>3)
  mm.seek(0)
  show_img(seed * vw * vh)

def fill_scr_ani(event=None, delay=1/30):
  ''' R - G - B transition animation, 30fps delay = 1/30 sec by default '''
  from time import sleep
  while not event or not event.is_set():
    for i in range(256):
      if event and event.is_set(): event.clear(); return
      fill_scr(i, 255-i, 255) # abc
      sleep(delay)
    for i in range(256):
      if event and event.is_set(): event.clear(); return
      fill_scr(255, i, 255-i) # cab
      sleep(delay)
    for i in range(256):
      if event and event.is_set(): event.clear(); return
      fill_scr(255-i, 255, i) # bca
      sleep(delay)

def black_scr():
  fill_scr(0,0,0)

def white_scr():
  fill_scr(255,255,255)

def mmseekto(x,y):
  mm.seek((x + y*w) * bytepp)

def dot(x, y, r, g, b):
  mmseekto(x,y)
  mm.write(struct.pack('BBB',*((r,g,b) if RGB else (b,g,r))))

def get_pixel(x,y):
  mmseekto(x,y)
  return mm.read(bytepp)

# GIF should have BGR format data
def ready_img(fpath, resize=True):
  from PIL import Image
  im = Image.open(fpath)
  return im.resize((vw,vh), ANTIALIAS) if resize else im

def _888_to_565(bt):
  b = b''
  for i in range(0, len(bt),3):
    b += int.to_bytes(bt[i]>>3<<11|bt[i+1]>>2<<5|bt[i+2]>>3, 2, 'little')
  return b

def numpy_888_565(bt):
  import numpy as np
  arr = np.fromstring(bt, dtype=np.uint32)
  return (((0xF80000 & arr)>>8)|((0xFC00 & arr)>>5)|((0xF8 & arr)>>3)).astype(np.uint16).tostring()

def show_img(img):
  if not type(img) is bytes:
    if not RGB:
      if bpp == 24: # for RPI
        img = img.tobytes('raw', 'BGR')
      else:
        img = img.convert('RGBA').tobytes('raw', 'BGRA')
        if bpp == 16:
          img = numpy_888_565(img)
          #img = img.tobytes('raw', 'BGR')
          #img = _888_to_565(img)
          #from io import BytesIO
          #bt = BytesIO(img)
          #for y in range(vh):
          #  mmseekto(vx,vy+y)
          #  for x in range(vw):
          #    b,g,r = [ord(bt.read(1)) for i in range(3)]
          #    mm.write(int.to_bytes(b>>3 | g>>2<<5 | r>>3<<11, 2, 'little'))
          #return
    else:
      if bpp == 24:
        img = img.tobytes()
      else:
        img = img.convert('RGBA').tobytes()
        if bpp == 16:
          img = numpy_888_565(img)
  from io import BytesIO
  b = BytesIO(img)
  s = vw*bytepp
  for y in range(vh): # virtual window drawing
    mmseekto(vx,vy+y)
    mm.write(b.read(s))

def _ready_gif(cut):
  dur = 1
  if cut.info.get('duration'):
    dur = cut.info['duration']/1000
  cut = cut.convert('RGBA' if bpp == 32 else 'RGB').resize((vw,vh), ANTIALIAS)
  if not RGB:
    return cut.tobytes('raw', 'BGRA' if bpp == 32 else 'BGR'), dur
  return cut.tobytes(), dur
    
def ready_gif(gif, preview=False):
  from PIL import ImageSequence
  #from multiprocessing import Pool
  imgs = []
  fm = ''
  for l in open('/proc/meminfo'):
    if l.startswith('MemFree:'):
      fm = int(l.split()[1])
      break
  frame_limit = fm // msize_kb
  for img in ImageSequence.Iterator(gif):
    imgs.append(_ready_gif(img))#.copy())
    if preview:
      preview = False
      show_img(imgs[0][0])
    if len(imgs) >= frame_limit:
      if _verbose:
        #print('This file is too big to play. Limited to play only %d frames in total %d frames.' % (frame_limit, gif.n_frames))
        print('This file is too big to play. Limited to play only %d frames.' % frame_limit )
      break
  #with Pool(4) as p:
    #imgs=list(p.map(_ready_gif, imgs))
  return imgs

def gif_loop(gif, event=None, force_loop=False, preview=False):
  from threading import Thread, Event, Timer
  from itertools import cycle
  imgs = ready_gif(gif, preview)
  if event is None : event = Event()
  for i in range(force_loop if type(force_loop) is int else 1):
    for img, dur in cycle(imgs) if force_loop is True else imgs:
      if event and event.is_set():
        return
      Timer(dur, lambda e:event.set(), [event]).start()
      show_img(img)
      event.wait() # wait for animation frame duration
      event.clear()

if __name__ == '__main__':
  print('This is a pure Python library file. If you want to use as stand-alone, use \'main.py\' instead.')
  exit(1)
