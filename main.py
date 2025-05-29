def on_overlap_tile(sprite, location):
    tiles.place_on_tile(mySprite, tiles.get_tile_location(2, 2))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
        """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    mySprite.say_text("he said :(", 1000, True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile6
        """),
    on_overlap_tile2)

def on_a_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e d d d d d d e e f . .
                . . . f e e 4 4 4 4 e e f . . .
                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . f f e 2 f f f f f f 2 e f f .
                . f f f f f e e e e f f f f f .
                . . f e f b f 4 4 f b f e f . .
                . . f e 4 1 f d d f 1 4 e f . .
                . . . f e 4 d d d d 4 e f e . .
                . . f e f 2 2 2 2 e d d 4 e . .
                . . e 4 f 2 2 2 2 e d d e . . .
                . . . . f 4 4 5 5 f e e . . . .
                . . . . f f f f f f f . . . . .
                . . . . f f f . . . . . . . . .
                """),
            img("""
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e d d d d d d e e f . .
                . . . f e e 4 4 4 4 e e f . . .
                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f e e 2 2 2 2 2 2 e f f . .
                . f f e 2 f f f f f f 2 e f f .
                . f f f f f e e e e f f f f f .
                . . f e f b f 4 4 f b f e f . .
                . . f e 4 1 f d d f 1 4 e f . .
                . . e f e 4 d d d d 4 e f . . .
                . . e 4 d d e 2 2 2 2 f e f . .
                . . . e d d e 2 2 2 2 f 4 e . .
                . . . . e e f 5 5 4 4 f . . . .
                . . . . . f f f f f f f . . . .
                . . . . . . . . . f f f . . . .
                """)],
        100,
        True)
    if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite.vy = -120
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile3(sprite3, location3):
    mySprite.say_text("spikes and water kill you", 1000, True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile4
        """),
    on_overlap_tile3)

def on_combos_attach_combo():
    game.game_over(True)
controller.combos.attach_combo("up up down down left right left right b a",
    on_combos_attach_combo)

def on_left_pressed():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    animation.run_image_animation(mySprite,
        [img("""
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e e f f . . . .
                . . . f 2 2 2 e d d 4 . . . . .
                . . . f 2 2 2 e d d e . . . . .
                . . . f 5 5 4 f e e f . . . . .
                . . . . f f f f f f . . . . . .
                . . . . . . f f f . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d e e e e e f . . .
                . . . f e 4 e d d 4 f . . . . .
                . . . f 2 2 e d d e f . . . . .
                . . f f 5 5 f e e f f f . . . .
                . . f f f f f f f f f f . . . .
                . . . f f f . . . f f . . . . .
                """),
            img("""
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e e f f . . . .
                . . . f 2 2 2 e d d 4 . . . . .
                . . . f 2 2 2 e d d e . . . . .
                . . . f 5 5 4 f e e f . . . . .
                . . . . f f f f f f . . . . . .
                . . . . . . f f f . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e d d 4 . . . .
                . . . f 2 2 2 2 e d d e . . . .
                . . f f 5 5 4 4 f e e f . . . .
                . . f f f f f f f f f f . . . .
                . . . f f f . . . f f . . . . .
                """)],
        100,
        False)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile4(sprite4, location4):
    global mySprite2
    tiles.set_current_tilemap(tilemap("""
        level3
        """))
    tiles.place_on_tile(mySprite, tiles.get_tile_location(2, 2))
    mySprite2 = sprites.create(assets.image("""
        evil bob
        """), SpriteKind.enemy)
    mySprite2.follow(mySprite, 100)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        happy bob
        """),
    on_overlap_tile4)

def on_right_pressed():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . f f e e 4 4 4 e f . . .
                . . . . . 4 d d e 2 2 2 f . . .
                . . . . . e d d e 2 2 2 f . . .
                . . . . . f e e f 4 5 5 f . . .
                . . . . . . f f f f f f . . . .
                . . . . . . . f f f . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e e e d d d f . . .
                . . . . . f 4 d d e 4 e f . . .
                . . . . . f e d d e 2 2 f . . .
                . . . . f f f e e f 5 5 f f . .
                . . . . f f f f f f f f f f . .
                . . . . . f f . . . f f f . . .
                """),
            img("""
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . f f e e 4 4 4 e f . . .
                . . . . . 4 d d e 2 2 2 f . . .
                . . . . . e d d e 2 2 2 f . . .
                . . . . . f e e f 4 5 5 f . . .
                . . . . . . f f f f f f . . . .
                . . . . . . . f f f . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . 4 d d e 4 4 4 e f . . .
                . . . . e d d e 2 2 2 2 f . . .
                . . . . f e e f 4 4 5 5 f f . .
                . . . . f f f f f f f f f f . .
                . . . . . f f . . . f f f . . .
                """)],
        100,
        False)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_overlap_tile5(sprite5, location5):
    tiles.place_on_tile(mySprite, tiles.get_tile_location(2, 8))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile5
        """),
    on_overlap_tile5)

def on_overlap_tile6(sprite6, location6):
    tiles.set_current_tilemap(tilemap("""
        level2
        """))
    tiles.place_on_tile(mySprite, tiles.get_tile_location(2, 2))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        sad bob
        """),
    on_overlap_tile6)

mySprite2: Sprite = None
mySprite: Sprite = None
tiles.set_current_tilemap(tilemap("""
    tutorial
    """))
scene.set_background_color(9)
mySprite = sprites.create(img("""
        . . . . . . f f f f f f . . . .
        . . . . f f e e e e f 2 f . . .
        . . . f f e e e e f 2 2 2 f . .
        . . . f e e e f f e e e e f . .
        . . . f f f f e e 2 2 2 2 e f .
        . . . f e 2 2 2 f f f f e 2 f .
        . . f f f f f f f e e e f f f .
        . . f f e 4 4 e b f 4 4 e e f .
        . . f e e 4 d 4 1 f d d e f . .
        . . . f e e e 4 d d d d f . . .
        . . . . f f e e 4 4 4 e f . . .
        . . . . . 4 d d e 2 2 2 f . . .
        . . . . . e d d e 2 2 2 f . . .
        . . . . . f e e f 4 5 5 f . . .
        . . . . . . f f f f f f . . . .
        . . . . . . . f f f . . . . . .
        """),
    SpriteKind.player)
mySprite.ay = 200
tiles.place_on_tile(mySprite, tiles.get_tile_location(2, 2))
scene.camera_follow_sprite(mySprite)
controller.move_sprite(mySprite, 100, 0)