import java.io.BufferedReader

import java.io.InputStreamReader

fun main(){
    val br = BufferedReader(InputStreamReader(System.`in`))

    val str = br.readLine()
    var answer = Integer.MAX_VALUE

    var cntA = 0

    for(i in 0 until str.length){
        if(str[i] == 'a')
            cntA++
    }

    for(i in 0 until str.length){
        var cntB = 0
        for(j in i until i+cntA){
            val idx = j % str.length

            if(str[idx] == 'b')
                cntB++
        }

        answer = Math.min(answer, cntB)
    }

    print(answer)
}