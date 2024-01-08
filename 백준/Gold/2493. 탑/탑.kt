import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter
import java.util.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    br.readLine()
    val list = br.readLine().split(" ").map { it.toInt() }

    val dq = ArrayDeque<List<Int>>()

    for ((i, h) in list.withIndex()) {
        while(!dq.isEmpty()){
            if(dq.peekLast()[1] >= h){
                bw.write("${dq.peekLast()[0]+1}")
                break;
            }

            dq.removeLast()
        }

        if(dq.isEmpty())
            bw.write("0")
        
        if(i < list.size-1)
            bw.write(" ")

        dq.add(listOf(i, h))
    }

    bw.flush()
}


