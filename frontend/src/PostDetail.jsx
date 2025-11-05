import React from "react"
import { useParams } from "react-router-dom"

export default function(){
    const param = useParams()
    const [post,setPost] = React.useState({})
    const [error,setError] = React.useState(null)
    const [isLoading, setLoading] = React.useState(true)
    React.useEffect(()=>{
        fetch(`/api/posts/${param.slug}/`)
        .then( res=> {
            if(!res.ok){
                throw new Error(`HTTP error! status: ${res.status}`)
            }
            return res.json()
        })
        .then(data => setPost(data))
        .catch(err => setError(err.message))
        .finally(()=>setLoading(false))
    },[param.slug])


   
   if(isLoading){
    return <div>loading...</div>
   }
   if(error){
    return <div>{error}</div>
   }
    return (
        <div>
           <h1> {post.title}</h1>
           <h2>{post.body}</h2>
        </div>
    )
}