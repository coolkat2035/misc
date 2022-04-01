import pygame, random

pygame.init()

WIDTH, HEIGHT = 800, 600
LOGO_SIZE = (100, int(1305/2560*100))#og 2560, 1305

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("professional time waster")

clock = pygame.time.Clock()

dvd = pygame.image.load("dvdLogo/le_logo.png")
dvd = pygame.transform.scale(dvd, LOGO_SIZE)

dvd_white = dvd.copy()
                             
x, y = WIDTH//2, HEIGHT//2
vX, vY = random.randint(1,5), random.randint(1,5)

def changeColor(image, color):
    coloredImage = pygame.Surface(image.get_size())
    coloredImage.fill(color)
    
    finalImage = image.copy()
    finalImage.blit(coloredImage, (0, 0), special_flags = pygame.BLEND_RGBA_MULT)
    return finalImage
  
run = True
while run:
  clock.tick(60)
  window.fill((0,0,0))
    
  for event in pygame.event.get():
    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
      #press anything to quit
      run = False

  if x not in range(0, WIDTH - LOGO_SIZE[0]+1):#bouncy
    vX = vX * -1#(vX + random.randint(-1,1)) * -1#speed up/down a bit, then reverse direction...
    if vX > 7:
      vX -= random.randint(2,5)
    elif vX < -7:
      vX += random.randint(2,5)
    dvd = changeColor(dvd_white, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    
  if y not in range(0, HEIGHT - LOGO_SIZE[1]+1):
    vY = vY * -1#(vY + random.randint(-1,1)) * -1
    if vY > 7:
      vY -= random.randint(2,5)
    elif vY < -7:
      vY += random.randint(2,5)
    dvd = changeColor(dvd_white, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))

      
  x += vX
  y += vY

  window.blit(dvd, (x,y))
  print(x, y, vX,vY)
  pygame.display.flip()
  
pygame.quit()
print(LOGO_SIZE)
