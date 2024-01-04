import java.io.BufferedReader

import java.io.InputStreamReader

fun main(){
    val br = BufferedReader(InputStreamReader(System.`in`))

    val (N, d, k, c) = br.readLine().split(" ").map{it.toInt()}
    val list = ArrayList<Int>()
    var answer = 0

    for(i in 0 .. N-1){
        list.add(br.readLine().toInt())
    }

    val set = HashSet<Int>()
    val num = Array(3001){0}
    var start = 0
    var end = 0

    num[list[0]]++
    set.add(list[0])

    while(true){
        val cnt = end - start + 1

        if(cnt > k){
            num[list[start]]--
            if(num[list[start]] == 0)
                set.remove(list[start])
            start++
        }

        var noc = set.count()

        if(!set.contains(c))
            noc++

        if(noc > answer){
            answer = noc
        }


        if(start == N)
            break

        end++
        num[list[end%N]]++
        set.add(list[end % N])
    }

    print(answer)
}