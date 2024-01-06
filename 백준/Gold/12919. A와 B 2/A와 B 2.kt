import java.io.BufferedReader

import java.io.InputStreamReader

var target: String? = null
fun main(){
    val br = BufferedReader(InputStreamReader(System.`in`))

    target = br.readLine()
    val str = StringBuilder(br.readLine())

    if(target==str.toString() ||dfs(str))
        print(1)
    else
        print(0)
}

fun dfs(str: StringBuilder):Boolean{
    if(str.toString() == target)
        return true

    if(str.length <= (target?.length ?: 0)){
        return false
    }

    if(str[str.length-1] == 'A'){
        if(dfs(StringBuilder(str).deleteCharAt(str.length-1)))
            return true

    }

    if(str[0] == 'B'){
        if(dfs(StringBuilder(str).deleteCharAt(0).reverse()))
            return true
    }

    return false
}