float mean(float[] sequence) {
  
    float sum = 0;
    for (int i = 0; i < sequence.length; i++) {
        sum = sum + sequence[i];
    }
     return sum/sequence.length;
 }
float[] values = {10, 9, 73, 25, 33, 76, 52, 1, 35, 86};
void setup() {
    println(mean(values));
  }
  
  
  void setup() {
    size(200,100);
    printIn(mean(values));
  }
  



    
