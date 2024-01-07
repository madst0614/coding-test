import java.io.*
import kotlin.math.max
import kotlin.math.min


fun main(){
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    val T = br.readLine().toInt()

    for(t in 0 until T){
        val str = br.readLine()
        val K = br.readLine().toInt()

        val list = Array(26){ArrayList<Int>()}

        for((i,c) in str.withIndex()){
            list[c-'a'].add(i)
        }

        var s = Integer.MAX_VALUE
        var l = -1

        for(i in 0 until 26){
            if(list[i].count() >= K){
                var start = 0

                for(end in list[i].indices){
                    if(end-start+1 > K){
                        start++
                    }

                    if(end-start+1==K){
                        val length = list[i][end]-list[i][start]+1

                        s = min(s, length)
                        l = max(l, length)
                    }

                }
            }
        }

        if(l == -1){
            bw.write("-1\n")
        }
        else{
            bw.write("$s $l\n")
        }
    }

    bw.flush()
}
