import  React from "react"
import { Link } from "react-router-dom"
export default function All_Posts() {
  const [posts,setPosts] = React.useState([])
  const [isLoading,setLoading] = React.useState(true)
  const [error,setError] = React.useState(null)

  React.useEffect(()=>{
    fetch("/api/posts/")
    .then(res=> {
        if(!res.ok){
            throw new Error(`HTTP error! status: ${res.status}`)
        }
        return res.json()
    })
    .then(data=>setPosts(data))
    .catch(err => setError(err.message))
    .finally(() => setLoading(false))
  },[])

    const all_posts = posts.map(post=>{
      return (
        <div>
          <Link to={`/posts/${post.slug}`}><h1>{post.title}</h1></Link>
          <h2>{post.body}</h2>
          <h3>{post.author}</h3>
        </div>
      )
    })
        
        if(isLoading){
            return <div>loading...</div>
        }
        if(error){
            return <div>{error}</div>
        }
       
      return(
            <div>
             {all_posts}
            </div>
      )
}

