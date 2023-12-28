import java.io.BufferedWriter
import java.io.OutputStreamWriter

val dr = listOf(-1, 1, 0, 0)
val dc = listOf(0 , 0, -1, 1)


fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {

    val bw = BufferedWriter(OutputStreamWriter(System.out))

    val (N, K) = readln().split(" ").map{it.toInt()}

    val num = Array<Int>(100_001){0}

    val list = readln().split(" ").map{it.toInt()}

    var s=0

    var answer = 0;

    for (i in 0..<list.count()){
        num[list[i]]++


        while(num[list[i]]>K){
            num[list[s]]--
            s++
        }

        if(i-s+1>answer)
            answer = (i-s + 1)
    }


    print(answer)
}
