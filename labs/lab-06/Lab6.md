# Lab 6

<hr />

## Step 1:

Modified Code, see [Lab6p1](Lab6p1.py) for full code:

    if __name__ == '__main__':
        for (source, target) in [('chaos', 'order'),
                             ('nodes', 'graph'),
                             ('moron', 'smart'),
                             ('flies', 'swims'),
                             ('mango', 'peach'),
                             ('pound', 'marks')]:

i.

    Shortest path between chaos and order is
    chaos
    choos
    shoos
    shoes
    shoed
    shred
    sired
    sided
    aided
    added
    adder
    odder
    order

ii.

    Shortest path between nodes and graph is
    nodes
    lodes
    lores
    lords
    loads
    goads
    grads
    grade
    grape
    graph

iii.

    Shortest path between moron and smart is
    moron
    boron
    baron
    caron
    capon
    capos
    capes
    canes
    banes
    bands
    bends
    beads
    bears
    sears
    stars
    start
    smart

iv.

    Shortest path between flies and swims is
    flies
    flips
    slips
    slims
    swims

v.

    Shortest path between mango and peach is
    mango
    mange
    marge
    merge
    merse
    terse
    tease
    pease
    peace
    peach

vi.

    Shortest path between pound and marks is
    None

<hr />

## Step 3:

Modified Code, see [Lab6p3](Lab6p3.py) for full code:

    def words_graph():
        fh = gzip.open('words4_dat.txt.gz', 'r')
        w = str(line[0:4])

    if __name__ == '__main__':
        for (source, target) in [('cold', 'warm'),
                                 ('love', 'hate'),
                                 ('good', 'evil'),
                                 ('pear', 'beef'),
                                 ('make', 'take')]:

i.

    Shortest path between cold and warm is
    cold
    wold
    word
    ward
    warm

ii.

    Shortest path between love and hate is
    love
    hove
    have
    hate

iii.

    Shortest path between good and evil is
    None

iv.

    Shortest path between pear and beef is
    pear
    bear
    beer
    beef

v.

    Shortest path between make and take is
    make
    take

<hr />

## Step 4:

Modified Code:
[Part Four Code](lab6p4.py)

i.

    Shortest path between chaos and order is
    chaos
    chose
    chore
    coder
    order


ii.

    Shortest path between nodes and graph is
    nodes
    anode
    agone
    anger
    gaper
    graph


iii.

    Shortest path between moron and smart is
    moron
    manor
    roams
    smart


iv.

    Shortest path between flies and swims is
    flies
    isles
    semis
    swims


v.

    Shortest path between mango and peach is
    mango
    conga
    nacho
    poach
    peach


vi.
    
    Shortest path between pound and marks is
    pound
    mound
    monad
    moans
    roams
    marks
