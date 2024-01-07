import java.io.*


fun main(){
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    val T = br.readLine().toInt()

    for(t in 0 until T){
        val str = br.readLine()
        val K = br.readLine().toInt()

        val list = Array<ArrayList<Int>>(26){ArrayList<Int>()}

        for(i in str.indices){
            list[str[i]-'a'].add(i)
        }

        var s = Integer.MAX_VALUE
        var l = -1

        for(i in str.indices){
            val c = str[i]-'a'

            if(list[c].count() >= K){
                var start = 0

                for(end in list[c].indices){
                    if(end-start+1 > K){
                        start++
                    }

                    if(end-start+1==K){
                        val length = list[c][end]-list[c][start]+1

                        s = Math.min(s, length)
                        l = Math.max(l, length)
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
