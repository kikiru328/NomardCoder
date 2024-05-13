from typing import Any


class Dog:
    def __init__(self, name):
        self.name = name
        
    def __str__(self): # 클래스가 문자열로 보이게 끔. #내부적으로 자동으로 사용
        return f"Dog : {self.name}"
    
    def __getattribute__(self, name: str) -> Any:
        print(f'they want to get {name}')
        return "😁"

owal = Dog('owal')
print(owal.name) # 객체, 메모리 위치
bok = Dog("Bok Dol")
print(bok.name)

# print(dir(Dog)) # 클래스와 속성, method를 출력