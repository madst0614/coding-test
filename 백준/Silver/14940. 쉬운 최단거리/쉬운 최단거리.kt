import java.io.BufferedWriter
import java.io.OutputStreamWriter

val dr = listOf(-1, 1, 0, 0)
val dc = listOf(0 , 0, -1, 1)

fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {

    val bw = BufferedWriter(OutputStreamWriter(System.out))

    val (n, m) = readln().split(" ").map { it.toInt() }

    var map = Array<Array<Int>>(n){Array<Int>(m){ 0 } }
    var answer = Array<Array<Int>>(n){Array<Int>(m){ 0 } }

    val q = ArrayDeque<Int>()

    var (ei, ej) = Pair(0, 0)
    for(i in 0..<n){
        val tmp = readln().split(" ")
        for(j in 0..<m){
            map[i][j] = tmp[j].toInt()

            if(map[i][j] ==1)
                answer[i][j] = -1

            if(map[i][j] == 2){
                ei=i
                ej=j
            }
        }
    }

    q.add(ei)
    q.add(ej)
    q.add(0)

    while(!q.isEmpty()){
        val r = q.removeFirst()
        val c = q.removeFirst()
        val cnt = q.removeFirst()

        for(i in 0..3){
            val nr = r + dr[i]
            val nc = c + dc[i]

            if(valid(nr, nc, n, m) && map[nr][nc] ==1 && answer[nr][nc]==-1){
                answer[nr][nc] = cnt+1
                q.addLast(nr)
                q.addLast(nc)
                q.addLast(cnt+1)
            }
        }
    }

    for(i in 0..<n){
        for(j in 0..<m){
            bw.write("${answer[i][j]}")
            if(j < m-1)
                bw.write(" ")
        }

        bw.write("\n")
    }

    bw.flush()
}

fun valid(r:Int, c:Int, n:Int, m:Int):Boolean{
    return r in 0..<n && c in 0..<m;
}