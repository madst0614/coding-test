import java.io.BufferedWriter
import java.io.OutputStreamWriter

val dp = Array(10_001){Integer.MAX_VALUE}


fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {

    val bw = BufferedWriter(OutputStreamWriter(System.out))

    val (N,D) = readln().split(" ").map{it.toInt()}

    val arr = ArrayList<List<Int>>()

    for( i in 0..<N){
        val tmp:List<Int> = readln().split(" ").map{it.toInt()}

        arr.add(tmp)
    }

    arr.sortWith(Comparator<List<Int>>{
        a,b ->
        if(a[0] == b[0]) a[1]-b[1]
        else a[0]-b[0]

    })

    dp[0] = 0
    var idx = 1

    for(i in 0..<arr.size){
        val list = arr[i]

        while(idx <= list[0]){
            dp[idx] = Math.min(dp[idx],dp[idx-1]+1)
            idx++
        }


        dp[list[1]] = Math.min(dp[list[1]], dp[list[0]] + list[2])

    }

    while(idx<=D){
        dp[idx] = Math.min(dp[idx],dp[idx-1]+1)
        idx++
    }

    print(dp[D])
}


