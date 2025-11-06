import  React from "react"
import { Link } from "react-router-dom"
export default function All_Posts() {
  const [posts,setPosts] = React.useState([])
  const [isLoading,setLoading] = React.useState(true)
  const [next,setNext] = React.useState(null)
  const [previous,setPrevious] = React.useState(null)
  const [error,setError] = React.useState(null)
  const [count,setCount] = React.useState(0)
  const [currentPage,setCurrentPage] = React.useState(1)

  const [url,setUrl] = React.useState("/api/posts/?page=1")
  
  React.useEffect(()=>{
    setLoading(true)
    fetch(url)
    .then(res=> {
        if(!res.ok){
            throw new Error(`HTTP error! status: ${res.status}`)
        }
        return res.json()
    })
    .then(data=>{
        console.log(data)
        setNext(data.next) 
        setPrevious(data.previous)
        setCount(data.count)
        setPosts(data.results)
    })
    .catch(err => setError(err.message))
    .finally(() => setLoading(false))
  },[url])


   function updateUrl(url){
    const current = new URL(url,window.location.origin)
    setCurrentPage(Number(current.searchParams.get("page")))
       setUrl(url)
   }
    const all_posts = posts.map(post=>{
      return (
        <div key={post.id}>
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
             <div>
                {previous && <button onClick={()=>updateUrl(previous)}>Previous</button>}
                <span>page {currentPage} of {Math.ceil(count/5)}</span> 
                {next && <button onClick={()=>updateUrl(next)}>next</button>}

             </div>
            </div>
      )
}

