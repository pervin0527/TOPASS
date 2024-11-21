 ```cpp
 g++ -std=c++17 -o ./builds/array_vector 01_array_vector.cpp
 ```


```cpp
ios::sync_with_studio(0)
cint.tie(0)
```

- ```ios::sync_with_studio(0)```는 C stream과 C++ stream의 동기화를 해제시켜 입출력 속도를 더 빠르게 만든다.
- ```cin.tie(0)```은 cin 실행 전에 cout 버퍼를 비우게하는 것을 수행하지 않게 하여 속도를 증가시킨다. 코테에서는 버퍼를 비우는 것이 시간낭비.