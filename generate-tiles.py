
"""
"""

class Group:
    Unknown         =  0
    NonMetal        =  1
    Halogen         =  2
    NobleGas        =  3 
    class Metal:
        Alkali      =  4
        AlkaliEarth =  5
        Lanthanide  =  6
        Actinide    =  7
        Trans       =  8
        PostTrans   =  9
        Metalloid   = 10

class Element:
    def __init__(self, number, symbol, name, weight, group, color=None):
        self.number = number
        self.symbol = symbol
        self.name = name
        self.weight = weight
        self.group = group
        if color is None:
            if group == Group.NonMetal:
                color = (0xff,0xff,0xff)
            elif group == Group.NobleGas:
                color = (0xff,0xff,0xff)
            else:
                color = (0xC0,0xC0,0xC0)
        self.color = color
    def __repr__(self):
        return '%s(%u)' % (self.name, self.number)

elements = [
    Element(  1, "H",  "Hydrogen",     "1.0.7594",       Group.NonMetal),
    Element(  2, "He", "Helium",       "4.002602",       Group.NobleGas),
    Element(  3, "Li", "Lithium",      "6.941(2)",       Group.Metal.Alkali,     (0xcf,0xcf,0xc3)),
    Element(  4, "Be", "Beryllium",    "9.012182(3)",    Group.Metal.AlkaliEarth),
    Element(  5, "B",  "Boron",        "10.811(7)",      Group.Metal.Metalloid,  (0x80,0x80,0x80)),
    Element(  6, "C",  "Carbon",       "12.0107(8)",     Group.NonMetal,         (0x40,0x40,0x40)),
    Element(  7, "N",  "Nitrogen",     "14.00.75(2)",    Group.NonMetal),
    Element(  8, "O",  "Oxygen",       "15.9994(3)",     Group.NonMetal,         (0xe5,0xe5,0xf9)),
    Element(  9, "F",  "Fluorine",     "18.9984032(5)",  Group.Halogen,          (0xf1,0xe2,0x92)),
    Element( 10, "Ne", "Neon",         "20.1797(6)",     Group.NobleGas),
    Element( 11, "Na", "Sodium",       "22.98976928(2)", Group.Metal.Alkali),
    Element( 12, "Mg", "Magnesium",    "24.3050(6)",     Group.Metal.AlkaliEarth),
    Element( 13, "Al", "Aluminum",     "26.9815386(13)", Group.Metal.Trans),
    Element( 14, "Si", "Silicon",      "28.0855(3)",     Group.Metal.Metalloid,  (0x7e,0x7e,0x83)),
    Element( 15, "P",  "Phosphorus",   "30.973762(2)",   Group.NonMetal,         (0xc8,0x00,0x00)),
    Element( 16, "S",  "Sulfur",       "32.065(5)",      Group.NonMetal,         (0xef,0xe1,0x00)),
    Element( 17, "Cl", "Chlorine",     "35.453(2)",      Group.Halogen,          (0xe2,0xea,0xa2)),
    Element( 18, "Ar", "Argon",        "39.948(1)",      Group.NobleGas),
    Element( 19, "K",  "Potassium",    "39.0983(1)",     Group.Metal.Alkali),
    Element( 20, "Ca", "Calcium",      "40.078(4)",      Group.Metal.AlkaliEarth),
    Element( 21, "Sc", "Scandium",     "44.955912(6)",   Group.Metal.Trans,      (0xd1,0xd1,0xbb)),
    Element( 22, "Ti", "Titanium",     "47.867(1)",      Group.Metal.Trans),
    Element( 23, "V",  "Vanadium",     "50.9415(1)",     Group.Metal.Trans,      (0x8c,0x8c,0x8d)),
    Element( 24, "Cr", "Chromium",     "51.9961(6)",     Group.Metal.Trans,      (0xe7,0xe7,0xe7)),
    Element( 25, "Mn", "Manganese",    "54.938045(5)",   Group.Metal.Trans,      (0x9d,0x95,0x95)),
    Element( 26, "Fe", "Iron",         "55.845(2)",      Group.Metal.Trans),
    Element( 27, "Co", "Cobalt",       "58.933195(5)",   Group.Metal.Trans,      (0x9f,0x9f,0xa1)),
    Element( 28, "Ni", "Nickel",       "58.6934(4)(2)",  Group.Metal.Trans),
    Element( 29, "Cu", "Copper",       "63.546(3)",      Group.Metal.Trans,      (0xC9,0x63,0x33)),
    Element( 30, "Zn", "Zinc",         "65.38(2)(4)",    Group.Metal.Trans,      (0x9f,0x9f,0xb0)),
    Element( 31, "Ga", "Gallium",      "69.723(1)",      Group.Metal.PostTrans),
    Element( 32, "Ge", "Germanium",    "72.63(1)",       Group.Metal.Metalloid,  (0x60,0x60,0x60)),
    Element( 33, "As", "Arsenic",      "74.92160(2)",    Group.Metal.Metalloid),
    Element( 34, "Se", "Selenium",     "78.96",          Group.NonMetal,         (0x50,0x50,0x50)),
    Element( 35, "Br", "Bromine",      "79.904(1)",      Group.Halogen,          (0xc6,0x55,0x00)),
    Element( 36, "Kr", "Krypton",      "83.798",         Group.NobleGas),
    Element( 37, "Rb", "Rubidium",     "85.4678(3)",     Group.Metal.Alkali,     (0xc0,0xc0,0xc6)),
    Element( 38, "Sr", "Strontium",    "87.62",          Group.Metal.AlkaliEarth),
    Element( 39, "Y",  "Yttrium",      "88.90585",       Group.Metal.Trans,      (0xa9,0xa9,0x90)),
    Element( 40, "Zr", "Zirconium",    "91.224",         Group.Metal.Trans),
    Element( 41, "Nb", "Niobium",      "92.90638",       Group.Metal.Trans),
    Element( 42, "Mo", "Molybdenum",   "95.96(2)",       Group.Metal.Trans,     (0x8c,0x8c,0x8d)),
    Element( 43, "Tc", "Technetium",   "98(0)",          Group.Metal.Trans),
    Element( 44, "Ru", "Ruthenium",    "101.07",         Group.Metal.Trans),
    Element( 45, "Rh", "Rhodium",      "102.90550",      Group.Metal.Trans),
    Element( 46, "Pd", "Palladium",    "106.42",         Group.Metal.Trans),
    Element( 47, "Ag", "Silver",       "107.8682",       Group.Metal.Trans,      (0xe3,0xe3,0xe3)),
    Element( 48, "Cd", "Cadmium",      "112.411",        Group.Metal.Trans,      (0x8f,0x8f,0x98)),
    Element( 49, "In", "Indium",       "114.818",        Group.Metal.PostTrans),
    Element( 50, "Sn", "Tin",          "118.710",        Group.Metal.PostTrans),
    Element( 51, "Sb", "Antimony",     "121.760(1)",     Group.Metal.Metalloid),
    Element( 52, "Te", "Tellurium",    "127.60",         Group.Metal.Metalloid),
    Element( 53, "I",  "Iodine",       "126.90447",      Group.Halogen,          (0x75,0x61,0x7e)),
    Element( 54, "Xe", "Xenon",        "131.293(6)",     Group.NobleGas),
    Element( 55, "Cs", "Cesium",       "132.9054519(2)", Group.Metal.Alkali),
    Element( 56, "Ba", "Barium",       "137.33",         Group.Metal.AlkaliEarth),
    # lanthanides
    Element( 57, "La", "Lanthanum",    "138.90547",      Group.Metal.Trans),
    Element( 58, "Ce", "Cerium",       "",               Group.Metal.Trans),
    Element( 59, "Pr", "Praseodymium", "",               Group.Metal.Trans),
    Element( 60, "Nd", "Neodymium",    "",               Group.Metal.Trans),
    Element( 61, "Pm", "Promethium",   "",               Group.Metal.Trans),
    Element( 62, "Sm", "Samarium",     "",               Group.Metal.Trans,     (0x7d,0x7d,0x5d)),
    Element( 63, "Eu", "Europium",     "",               Group.Metal.Trans,     (0x7c,0x7c,0x7c)),
    Element( 64, "Gd", "Gadolinium",   "",               Group.Metal.Trans),
    Element( 65, "Tb", "Terbium",      "",               Group.Metal.Trans),
    Element( 66, "Dy", "Dysprosium",   "",               Group.Metal.Trans),
    Element( 67, "Ho", "Holmium",      "",               Group.Metal.Trans,     (0x9e,0x9e,0x7c)),
    Element( 68, "Er", "Erbium",       "",               Group.Metal.Trans),
    Element( 69, "Tm", "Thulium",      "",               Group.Metal.Trans),
    Element( 70, "Yb", "Ytterbium",    "",               Group.Metal.Trans),
    Element( 71, "Lu", "Lutetium",     "",               Group.Metal.Trans),
    Element( 72, "Hf", "Hafnium",      "178.49",         Group.Metal.Trans),
    Element( 73, "Ta", "Tantalum",     "180.94788",      Group.Metal.Trans),
    Element( 74, "W",  "Tungsten",     "183.84",         Group.Metal.Trans),
    Element( 75, "Re", "Rhenium",      "186.207",        Group.Metal.Trans),
    Element( 76, "Os", "Osmium",       "190.23",         Group.Metal.Trans),
    Element( 77, "Ir", "Iridium",      "192.217",        Group.Metal.Trans),
    Element( 78, "Pt", "Platinum",     "195.084",        Group.Metal.Trans),
    Element( 79, "Au", "Gold",         "196.966569(4)",  Group.Metal.Trans,      (0xff,0xf3,0x2b)),
    Element( 80, "Hg", "Mercury",      "200.59(2)",      Group.Metal.Trans),
    Element( 81, "Tl", "Thallium",     "204.3833",       Group.Metal.PostTrans),
    Element( 82, "Pb", "Lead",         "207.2",          Group.Metal.PostTrans,  (0x85,0x85,0x85)),
    Element( 83, "Bi", "Bismuth",      "208.98040(1)",   Group.Metal.PostTrans,  (0xb7,0xaa,0xb7)),
    Element( 84, "Po", "Polonium",     "(209)",          Group.Metal.Metalloid),
    Element( 85, "At", "Astitine",     "(210)",          Group.Halogen),
    Element( 86, "Rn", "Radon",        "(222)",          Group.NobleGas),
    Element( 87, "Fr", "Francium",     "(223)",          Group.Metal.Alkali),
    Element( 88, "Ra", "Radium",       "(226.03)",       Group.Metal.AlkaliEarth),
    # actinides 
    Element( 89, "Ac", "Actinium",     "",               Group.Metal.Trans),
    Element( 90, "Th", "Thorium",      "",               Group.Metal.Trans,     (0x80,0x80,0x80)),
    Element( 91, "Pa", "Actinium",     "",               Group.Metal.Trans),
    Element( 92, "U",  "Uranium",      "238.02891(3)",   Group.Metal.Trans,     (0x85,0x85,0x85)),
    Element( 93, "Np", "Actinium",     "",               Group.Metal.Trans),
    Element( 94, "Pu", "Plutonium",    "(244)",          Group.Metal.Trans),
    Element( 95, "Am", "Americium",    "",               Group.Metal.Trans),
    Element( 96, "Cm", "Curium",       "",               Group.Metal.Trans),
    Element( 97, "Bk", "Berkelium",    "",               Group.Metal.Trans),
    Element( 98, "Cf", "Califorium",   "",               Group.Metal.Trans),
    Element( 99, "Es", "Einsteinium",  "",               Group.Metal.Trans),
    Element(100, "Fm", "Fermium",      "",               Group.Metal.Trans),
    Element(101, "Md", "Mendelevium",  "",               Group.Metal.Trans),
    Element(102, "No", "Nobelium",     "",               Group.Metal.Trans),
    Element(103, "Lr", "Lawrencium",   "",               Group.Metal.Trans),
    Element(104, "Rf", "Rutherfordium","[267]",          Group.Metal.Trans),
    Element(105, "Db", "Dubnium",      "[268]",          Group.Metal.Trans),
    Element(106, "Sg", "Seaborgium",   "[269]",          Group.Metal.Trans),
    Element(107, "Bh", "Bohrium",      "[270]",          Group.Metal.Trans),
    Element(108, "Hs", "Hassium",      "",               Group.Metal.Trans),
    Element(109, "Mt", "Meitnerium",   "",               Group.Metal.Trans),
    Element(110, "Ds", "Darmstadtium", "",               Group.Metal.Trans),
    Element(111, "Rg", "Roentgenium",  "",               Group.Metal.Trans),
    Element(112, "Cn", "Copernicium",  "",               Group.Metal.Trans),
    Element(113, "Uut","Ununtrium",    "",               Group.Metal.Trans),
    Element(114, "Uuq","Ununquadium",  "",               Group.Metal.Trans),
    Element(115, "Uup","Ununpentium",  "",               Group.Metal.Trans),
    Element(116, "Uuh","Ununhexium",   "",               Group.Metal.Trans),
    Element(117, "Uus","Ununseptium",  "",               Group.Metal.Trans),
    Element(118, "Uuo","Ununoctium",   "",               Group.Metal.Trans),
]

import cairo

def thicker(e, ctx, (r,g,b)):
    """the thicker parts of metals will be lighter colored (polished); gases will be darker because they're thicker"""
    if e.group in [Group.Metal.Trans, Group.Metal.PostTrans]:
        diff = +0.05
    else:
        diff = -0.05
    ctx.set_source_rgba(r+diff,g+diff,b+diff,0.5)

def img(e):

    size = 180
    border = 12
    r,g,b = e.color

    r = float(r) / 0xff
    g = float(g) / 0xff
    b = float(b) / 0xff

    width, height = size, size

    maxnamewidth = size - (border * 2) + 6

    # setup a place to draw
    #surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    surface = cairo.ImageSurface.create_from_png("img/sheetmetal.png")
    ctx = cairo.Context(surface)

    # paint background
    ctx.set_source_rgba(r,g,b,0.5)
    ctx.rectangle(0, 0, width, height)
    ctx.fill()

    #bg = cairo.ImageSurface.create_from_png("img/bg-metal.png")
    #ctx.set_source_surface(bg, width, height)
    #ctx.paint()

    # border
    ctx.set_source_rgba(0,0,0,0.1)
    ctx.set_line_width(border)
    ctx.rectangle(border/2+1, border/2+1, width-border, height-border)
    ctx.stroke()

    thicker(e, ctx, (r,g,b))
    ctx.set_line_width(border)
    ctx.rectangle(border/2, border/2, width-border, height-border)
    ctx.stroke()

    ####################

    s = str(e.number)
    ctx.select_font_face('Sans',
                cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(35)
    x_bearing, y_bearing, w, h = ctx.text_extents(s)[:4]
    ctx.move_to(160 - w, 45)
    ctx.set_source_rgba(0,0,0,0.2)
    ctx.show_text(s)

    x_bearing, y_bearing, w, h = ctx.text_extents(s)[:4]
    ctx.move_to(160 - w - 1, 44)
    thicker(e, ctx, (r,g,b))
    ctx.show_text(s)

    ####################

    s = e.symbol
    ctx.select_font_face('Century Schoolbook L',
                cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(80)
    x_bearing, y_bearing, w, h = ctx.text_extents(s)[:4]
    ctx.move_to((width - w) / 2.0, 110)
    ctx.set_source_rgba(0,0,0,0.2)
    ctx.show_text(s)

    x_bearing, y_bearing, w, h = ctx.text_extents(s)[:4]
    ctx.move_to(((width - w) / 2.0) - 1, 109)
    thicker(e, ctx, (r,g,b))
    ctx.show_text(s)

    ####################

    s = e.name
    ctx.select_font_face('Arial',
                cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(21)
    x_bearing, y_bearing, w, h = ctx.text_extents(s)[:4]

    if w >= maxnamewidth:
        ctx.set_font_size(20)
        ctx.select_font_face('Arial',
                cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        x_bearing, y_bearing, w, h = ctx.text_extents(s)[:4]

    ctx.move_to((width - w) / 2, 145)
    ctx.set_source_rgba(0,0,0,0.2)
    ctx.show_text(s)

    x_bearing, y_bearing, w, h = ctx.text_extents(s)[:4]
    ctx.move_to(((width - w) / 2) - 1, 144)
    thicker(e, ctx, (r,g,b))
    ctx.show_text(s)

    ####################

    """
    s = e.weight
    ctx.select_font_face('Sans',
                cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(18)
    x_bearing, y_bearing, w, h = ctx.text_extents(s)[:4]
    ctx.move_to((width - w) / 2.0, 165)
    ctx.set_source_rgba(0,0,0,0.2)
    ctx.show_text(s)

    x_bearing, y_bearing, w, h = ctx.text_extents(s)[:4]
    ctx.move_to(((width - w) / 2.0) - 1, 164)
    thicker(e, ctx, (r,g,b))
    ctx.show_text(s)
    """

    ####################

    # finish up
    ctx.stroke() # commit to surface
    surface.write_to_png('img/tile/%03u-%s.png' % (e.number, e.symbol))

if __name__ == '__main__':
    print elements
    for e in elements:
        img(e)

