#include <stdio.h>
#include <stdint.h>

#include <raylib.h>

#define HEIGHT 25*14
#define WIDTH  80*8

void _(){}

int main(){
  SetTraceLogCallback(_);
  InitWindow(WIDTH, HEIGHT, "REmu");
  
  while(!WindowShouldClose()){
    BeginDrawing();
      ClearBackground(BLACK);
    EndDrawing();
  }
  
  CloseWindow();
  return 0;
}