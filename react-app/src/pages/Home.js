import { useEffect } from "react";
import {useState} from 'react'
const Home = () => {
    const [articles, setArticles] = useState([]);
    useEffect(() => {
        fetch('http://localhost:3000/view')
        .then((res) => res.json())
        .then((res) => {
            console.log(res)
        })
    },[])
}

export default Home