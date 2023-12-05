import pygame

#define a class for animations
class AnimateSprite(pygame.sprite.Sprite):

    #define things to do when an entity is created
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'src/{sprite_name}.png')
        self.current_image = 0
        self.images = animations.get(sprite_name)

    #define a method to animate sprite
    def animate(self):

        #next image
        self.current_image += 1

        #verify if we have reached the last image
        if self.current_image >= len(self.images):
            #start animation over
            self.current_image = 0
            
        #replace previous animation image by the next
        self.image = self.images[self.current_image]
    

#define function to load a sprite
def load_animation_images(sprite_name):
    #load images from the sprite folder
    images = []
    #get the path from the sprite's folder
    path = f"src/{sprite_name}/{sprite_name}"

    #loop on each images in the folder
    for num in range(1, 13):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    #return the content of the image list
    return images

# define a dictionnary containing the loaded images
animations = {
    'skeleton' : load_animation_images('skeleton'),
    'boredhero_sword': load_animation_images('hero_sword_idle')
}

