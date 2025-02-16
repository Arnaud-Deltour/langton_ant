# ruff: noqa: D100,D103,I001,S101,PLR2004
import langton_ant as la


def test_ant_creation() -> None:
    ant = la.Ant(0,0,la.Dir.UP)
    assert ant.x == 0
    assert ant.y == 0
    assert ant.direction == la.Dir.UP

def test_ant_move() -> None:
    ant1 = la.Ant(0,0,la.Dir.UP)
    ant1.move()
    assert ant1.x == 0
    assert ant1.y == 1
    assert ant1.direction == la.Dir.UP

    ant2 = la.Ant(5,4,la.Dir.RIGHT)
    ant2.move()
    assert ant2.x == 6
    assert ant2.y == 4
    assert ant2.direction == la.Dir.RIGHT

    ant3 = la.Ant(-5,-8,la.Dir.LEFT)
    ant3.move()
    assert ant3.x == -6
    assert ant3.y == -8
    assert ant3.direction == la.Dir.LEFT

def test_ant_turn() -> None:
    ant = la.Ant(0,0,la.Dir.UP)
    ant.turn(la.Color.WHITE)
    assert ant.x == 0
    assert ant.y == 0
    assert ant.direction == la.Dir.RIGHT

    ant1 = la.Ant(0,0,la.Dir.UP)
    ant1.turn(la.Color.BLACK)
    assert ant1.x == 0
    assert ant1.y == 0
    assert ant1.direction == la.Dir.LEFT

