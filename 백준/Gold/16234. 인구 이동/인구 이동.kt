import java.io.*
import java.util.*
import kotlin.collections.ArrayDeque
import kotlin.math.abs
import kotlin.math.max
import kotlin.math.min

var N = 0
var L = 0
var R = 0
var map = Array(0){Array(0){0}}

val dr = listOf(0, 0, -1, 1)
val dc = listOf(1, -1, 0, 0)

fun main(){
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    val num = br.readLine().split(" ").map{it.toInt()}

    N = num[0]
    L = num[1]
    R = num[2]

    map = Array(N){Array(N){0}}

    for(i in map.indices){
        val str = br.readLine().split(" ").map{it.toInt()}
        for(j in map[i].indices){
            map[i][j] = str[j]
        }
    }

    var answer = 0

    while(true){
        var isMove = false
        val visited = Array(N){Array(N){false}}

        for(i in map.indices){
            for(j in map[i].indices){
                if(!visited[i][j]){
                    if(bfs(i,j, visited))
                        isMove = true
                }
            }
        }

        if(!isMove)
            break

        answer++
    }

    print(answer)
}

fun bfs(row: Int, col: Int, visited:Array<Array<Boolean>>): Boolean{
    val q = ArrayDeque<Int>()

    var total = 0
    val list = ArrayList<List<Int>>()

    q.add(row)
    q.add(col)

    while(!q.isEmpty()){
        val r = q.removeFirst()
        val c = q.removeFirst()

        if(visited[r][c])
            continue

        visited[r][c] = true
        total += map[r][c]
        list.add(listOf(r,c))

        for(i in 0 until 4){
            val nr = r + dr[i]
            val nc = c + dc[i]

            if( nr in 0 until N && nc in 0 until N && !visited[nr][nc]){
                if(abs(map[r][c] - map[nr][nc]) in L..R){
                    q.add(nr)
                    q.add(nc)
                }
            }
        }
    }

    for(loc in list){
        map[loc[0]][loc[1]] = total / list.count()
    }

    return list.count() > 1
}
