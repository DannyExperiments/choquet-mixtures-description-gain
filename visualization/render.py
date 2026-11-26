"""Render a rotating grid of the exact weighted three-atom example."""

import argparse
from math import cos, sin, tau
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


BG = "#101c30"
TEXT = "#f5f8fd"
MUTED = "#cbd7ed"
TEAL = "#78dcd1"
CORAL = "#ffac97"
ROWS = [(1/6,1/3,1/3), (1/3,1/6,1/3), (1/3,1/3,7/24)]
WEIGHTS = (1/2,1/4,1/4)
FACES = [(0,1,3,2),(4,6,7,5),(0,4,5,1),(2,3,7,6),(0,2,6,4),(1,5,7,3)]


def project(point, yaw):
    x,y,z = point
    rx = x*cos(yaw)+z*sin(yaw)
    rz = z*cos(yaw)-x*sin(yaw)
    tilt = .41+.15*cos(yaw)
    ry = y*cos(tilt)-rz*sin(tilt)
    depth = y*sin(tilt)+rz*cos(tilt)
    scale = 385/(5.5-depth)
    return 238+scale*rx, 272-scale*ry, depth


def shade(color, factor):
    rgb = tuple(int(color[i:i+2],16) for i in (1,3,5))
    return tuple(round(x*factor) for x in rgb)


def frame(angle, fonts):
    title, label, value, body = fonts
    result = Image.new("RGB",(880,580),BG)
    draw = ImageDraw.Draw(result)
    draw.text((26,22),"Later rows guarantee a density floor",font=title,fill=TEXT)
    draw.line((28,80,852,80),fill="#395375",width=2)
    draw.text((34,110),"Weighted entries",font=body,fill=MUTED)

    polygons = []
    for row, densities in enumerate(ROWS):
        for atom, density in enumerate(densities):
            x,z = 1.11*(atom-1), 1.11*(row-1)
            height = 11*WEIGHTS[row]*density
            points = [project((a,b,c),angle) for a in (x-.39,x+.39)
                      for b in (-.9,-.9+height) for c in (z-.39,z+.39)]
            color = CORAL if density<1/4 else TEAL
            for index, face in enumerate(FACES):
                vertices = [points[i] for i in face]
                depth = sum(p[2] for p in vertices)/4
                polygons.append((depth,vertices,shade(color,(.7,.8,.55,1,.64,.89)[index])))
    for _, vertices, fill in sorted(polygons):
        draw.polygon([p[:2] for p in vertices],fill=fill,outline=BG,width=2)

    draw.rounded_rectangle((445,106,853,441),radius=16,fill="#1a2b47")
    draw.text((468,124),"Atom",font=body,fill=MUTED)
    draw.text((548,124),"Last low row",font=body,fill=MUTED)
    draw.text((826,124),"Floor",font=body,fill=MUTED,anchor="ra")
    draw.line((468,175,831,175),fill="#395375",width=2)
    for index,(atom,last,floor) in enumerate((("A","1","1/8"),("B","2","1/16"),("C","0","1/4"))):
        y=195+74*index
        draw.text((478,y+4),atom,font=label,fill=TEXT)
        draw.text((640,y+4),last,font=label,fill=TEXT,anchor="ma")
        draw.text((825,y),floor,font=value,fill=TEAL,anchor="ra")

    for y,color,caption in ((471,CORAL,"Entry falls below 3/4 of its target"),
                            (521,TEAL,"Every later entry clears the threshold")):
        draw.ellipse((30,y+12,46,y+28),fill=color)
        draw.text((58,y),caption,font=body,fill=MUTED)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regular-font",default="DejaVuSans.ttf")
    parser.add_argument("--bold-font",default="DejaVuSans-Bold.ttf")
    parser.add_argument("--output",type=Path,default=Path("visualization/geometric-mixture.gif"))
    args=parser.parse_args()
    fonts=tuple(ImageFont.truetype(font,size) for font,size in (
        (args.bold_font,42),(args.bold_font,35),(args.bold_font,46),(args.regular_font,30)
    ))
    frames=[frame(.55+i*tau/64,fonts).quantize(colors=120,method=2) for i in range(64)]
    frames[0].save(args.output,save_all=True,append_images=frames[1:],
                   duration=92,loop=0,disposal=2,optimize=True)


if __name__ == "__main__":
    main()
