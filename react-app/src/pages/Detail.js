import { useEffect } from "react"
import {useState} from 'react'
const Detail = (props) => {
    console.log(props)
    const seq = props.match.params.seq

    const [article, setArticle] = useState({
        seq:``,
        title:``,
        article:``,
    })

    useEffect(() => {
        fetch('http://localhost:3000/article/' + seq)
        .then((res) => res.json)
        .then((res) => {
            setArticle(res)
        })
    },[])
    return (
        <div>
            <h1> 상세보기</h1>
            <hr/>
            <h3>{article.title}</h3>
            <h3>{article.article}</h3>
        </div>
    )
}
export default Detail