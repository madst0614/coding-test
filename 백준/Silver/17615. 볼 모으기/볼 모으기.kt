import java.io.BufferedWriter
import java.io.OutputStreamWriter

val dp = Array(10_001){Integer.MAX_VALUE}


fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {


    readln()
    val s = readln()

    var answer = Integer.MAX_VALUE

    answer = Math.min(answer, moveLeft('R', s))
    answer = Math.min(answer, moveRight('R', s))

    answer = Math.min(answer, moveLeft('B', s))
    answer = Math.min(answer, moveRight('B', s))


    print(answer)
}

fun moveLeft(c: Char, s:String):Int{
    var cnt:Int =0
    var cntStart = false

    for(i in s.count()-1 downTo 0){
        if(s[i] != c)
            cntStart = true
        else if(s[i] == c){
            if(cntStart)
                cnt++
        }
    }

    return cnt
}

fun moveRight(c: Char, s:String):Int{
    var cnt:Int =0
    var cntStart = false

    for(i in 0..<s.count()){
        if(s[i] != c)
            cntStart = true
        else if(s[i] == c){
            if(cntStart)
                cnt++
        }
    }

    return cnt
}


