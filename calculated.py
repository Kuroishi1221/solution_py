"""
Girl Don't Cry
Let's me know who you are please
I wanna know you phi-Code
"""
def main():
    """ Main function """
    animals, legs = 40, 88

    # Sees all animal
    pig = 0
    chicken = animals

    pig += (legs - chicken*2)//2
    chicken -= pig

    if pig*4 + chicken*2 == legs and animals*2 <= legs <= animals*4 and legs % 2 == 0:
        print('Pig = {}'.format(pig))
        print('Chicken = {}'.format(chicken))
        print('Total = {}'.format(chicken + pig))

"""
Radiohead - Creep
When you were here before
Couldn't look you in the eye
You're just like an angel
Your skin makes me cry
You float like a feather
In a beautiful world
And I wish I was special
You're so fuckin' special
But I'm a creep, I'm a weirdo.
What the hell am I doing here?
I don't belong here.
I don't care if it hurts
I want to have control
I want a perfect body
I want a perfect soul
I want you to notice
When I'm not around
You're so fuckin' special
I wish I was special
But I'm a creep, I'm a weirdo.
What the hell am I doing here?
I don't belong here.
She's running out again,
She's running out
She's run run run run
Whatever makes you happy
Whatever you want
You're so fuckin' special
I wish I was special
But I'm a creep, I'm a weirdo,
What the hell am I doing here?
I don't belong here.
I don't belong here."""
main()