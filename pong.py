import pygame
import sys

# Configurações do jogo
WIDTH, HEIGHT = 800, 600
BALL_SPEED = [4, 4]
PADDLE_SPEED = 6

# Inicializa o pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Raquetes e bola
ball = pygame.Rect(WIDTH//2 - 15, HEIGHT//2 - 15, 30, 30)
paddle1 = pygame.Rect(20, HEIGHT//2 - 60, 10, 120)
paddle2 = pygame.Rect(WIDTH - 30, HEIGHT//2 - 60, 10, 120)

# Pontuação
score1 = 0
score2 = 0

# Velocidade da bola
ball_speed = BALL_SPEED.copy()

# Função para desenhar os elementos
def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))
    
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"{score1}  {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH//2 - 30, 20))
    pygame.display.flip()

# Função para salvar pontuações
def salvar_pontuacao():
    with open("pontuacoes.txt", "a") as f:
        f.write(f"{score1} - {score2}\n")

# Loop principal
going = True
clock = pygame.time.Clock()
while going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salvar_pontuacao()
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += PADDLE_SPEED
    
    # Movimento da bola
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]
    
    # Colisão com paredes
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]
    
    # Colisão com raquetes
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] = -ball_speed[0]
    
    # Pontuação
    if ball.left <= 0:
        score2 += 1
        ball.x, ball.y = WIDTH//2 - 15, HEIGHT//2 - 15
        ball_speed = BALL_SPEED.copy()
    if ball.right >= WIDTH:
        score1 += 1
        ball.x, ball.y = WIDTH//2 - 15, HEIGHT//2 - 15
        ball_speed = [-BALL_SPEED[0], BALL_SPEED[1]]
    
    draw_objects()
    clock.tick(60)
