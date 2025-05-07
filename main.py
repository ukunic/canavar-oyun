import pygame, random

pygame.init()

GENISLIK, YUKSEKLIK = 700,600
pencere = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Canavar Oyunu")

pygame.mixer.music.load("C:\\Users\\user\\Desktop\\canavar_oyun\\assets\\oyunsarkisi.mp3")
pygame.mixer.music.play(-1, 0.0)
seviye_sesi = pygame.mixer.Sound("C:\\Users\\user\\Desktop\\canavar_oyun\\assets\\level.mp3")
yeme_sesi = pygame.mixer.Sound("C:\\Users\\user\\Desktop\\canavar_oyun\\assets\\yeme.wav")

HIZ = 10
saat = pygame.time.Clock()
FPS = 30

yem_gorseli = pygame.image.load("C:\\Users\\user\\Desktop\\canavar_oyun\\assets\\yem.png")
zehirli_yem_gorseli = pygame.image.load("C:\\Users\\user\\Desktop\\canavar_oyun\\assets\\zehirliyem.png")
arka_plan = pygame.image.load("C:\\Users\\user\\Desktop\\canavar_oyun\\assets\\arka_plan.jpg")

FONT = pygame.font.SysFont("consolas", 48)

skor = 0
buyudu = False
oyun_bitti = False

def oyunu_baslat():
    global canavar, canavar_rect, yem_rect, zehirli_yem_rect, skor, buyudu, oyun_bitti

    canavar = pygame.image.load("C:\\Users\\user\\Desktop\\canavar_oyun\\assets\\kucuk.png")
    canavar_rect = canavar.get_rect(center=(GENISLIK // 2, YUKSEKLIK // 2))

    yem_rect = yem_gorseli.get_rect(topleft=(150, 150))

    while True:
        zehirli_yem_rect = zehirli_yem_gorseli.get_rect(
            topleft=(random.randint(0, GENISLIK - 50), random.randint(100, YUKSEKLIK - 50))
        )
        if not zehirli_yem_rect.colliderect(canavar_rect):
            break

    skor = 0
    buyudu = False
    oyun_bitti = False

oyunu_baslat()

calisiyor = True
while calisiyor:
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            calisiyor = False

    if not oyun_bitti:
        tus = pygame.key.get_pressed()
        if tus[pygame.K_LEFT] and canavar_rect.left > 0:
            canavar_rect.x -= HIZ
        if tus[pygame.K_RIGHT] and canavar_rect.right < GENISLIK:
            canavar_rect.x += HIZ
        if tus[pygame.K_UP] and canavar_rect.top > 0:
            canavar_rect.y -= HIZ
        if tus[pygame.K_DOWN] and canavar_rect.bottom < YUKSEKLIK:
            canavar_rect.y += HIZ

        if canavar_rect.colliderect(yem_rect):
            yeme_sesi.play()
            yem_rect.x = random.randint(0, GENISLIK - 50)
            yem_rect.y = random.randint(100, YUKSEKLIK - 50)
            skor += 1

        if canavar_rect.colliderect(zehirli_yem_rect):
            oyun_bitti = True

        if skor > 6 and not buyudu:
            canavar = pygame.image.load("C:\\Users\\user\\Desktop\\canavar_oyun\\assets\\buyuk.png")
            seviye_sesi.play()
            eski_konum = canavar_rect.center
            canavar_rect = canavar.get_rect(center=eski_konum)
            buyudu = True

    pencere.blit(arka_plan, (0, 0))
    pencere.blit(yem_gorseli, yem_rect)
    pencere.blit(zehirli_yem_gorseli, zehirli_yem_rect)
    pencere.blit(canavar, canavar_rect)

    skor_yazi = FONT.render(f"Skor: {skor}", True, (255, 0, 0))
    pencere.blit(skor_yazi, (20, 20))
    pygame.draw.line(pencere, (255, 0, 255), (0, 90), (600, 90), 3)

    if oyun_bitti:
        bitis_yazi = FONT.render(f"Oyun Bitti! Skor: {skor}", True, (255, 255, 0))
        pencere.blit(bitis_yazi, (GENISLIK // 2 - bitis_yazi.get_width() // 2, YUKSEKLIK/ 2))

    pygame.display.update()
    saat.tick(FPS)

pygame.quit()
