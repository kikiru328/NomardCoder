# OOP : Object Oriented Programing

1. 코드를 정리하는 방식을 의미함.
2. Property : 속성 
3. Property가 중복되는 객체에 대해서 쉽게 정리가 가능함. >> Class
4. Class 는 일종의 구조를 보여줌.
5. Instance, Object >> Class를 이용한 이후에 나오는 것들로 이해
6. Method >> Class 내 있는 것들을 의미. (init : 자동 메서드)
7. self 는 class 내 property나 Method를 저장하는 방법
8. Inheritance : 코드 중복을 줄이고 재사용하게 함.
9. Super Method : Parent 의 Class를 사용하기 위함 (super.__init__)

# Concept
1. Abstraction
   1. 구현 세부 정보를 숨기는 일반 인터페이스를 지정하는 행위
   2. 각 메소드의 구현 세부 정보들을 가려서 실제 보이는 것과는 달리 세부 실현 정보들을 가릴 수가 있다.
2. Encapsulation
   1. 데이터, 데이터를 활용하는 함수를 캡슐, 컨테이너 안에 두는 것을 의미 (Class)
   2. 어떻게 클래스 정보에 접근 혹은 수정하는지를 결정하는 권한을 제공한다.
   3. "데이터 그리고 class 안에 있는 해당 데이터를 이용하는 함수를 잘 정리하는 방법론이다. 따라 원하는 데이터를 공유/보안을 설정할 수 있다.
3. Inheritance
   1. 클래스를 확장하면 자식 클래스는 부모 클래스의 모든 속성과 메소드를 상속 (수신)하게 됨.
   2. 조금더 코드를 정리하는 방법론
   3. 분할 및 정복을 가능하게 함.
4. Polymorphism
   1. method overriding을 이용하여 다른 method를 갖게끔 다양하게 확장함.
   2. 부모 클래스에서 메소드를 오버라이딩을 할 수 있지만, 부모 클래스의 규칙은 그대로 가져감 (string > string)