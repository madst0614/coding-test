import java.io.BufferedWriter
import java.io.OutputStreamWriter

val dp = Array(10_001){1}


fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {

    val bw = BufferedWriter(OutputStreamWriter(System.out))

    val T = readln().toInt()

    sol()

    for( i in 0..<T){
        val N = readln().toInt()

        bw.write("${dp[N]}\n")
    }

    bw.flush()
}

fun sol(){

    for(i in 3..10_000){
        dp[i] += dp[i-3]
    }

    for(i in 2 .. 10_000){
        dp[i] += dp[i-2]
    }
}
