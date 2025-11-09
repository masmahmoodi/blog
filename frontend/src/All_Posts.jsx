import React from "react"
import { Link, useSearchParams } from "react-router-dom"

export default function All_Posts() {
  const [posts, setPosts] = React.useState([])
  const [isLoading, setLoading] = React.useState(true)
  const [next, setNext] = React.useState(null)
  const [previous, setPrevious] = React.useState(null)
  const [error, setError] = React.useState(null)
  const [count, setCount] = React.useState(0)

  const [searchParams, setSearchParams] = useSearchParams()
  const startPage = Number(searchParams.get("page")) || 1
  const PAGE_SIZE = 5 

  const [currentPage, setCurrentPage] = React.useState(startPage)
  const [url, setUrl] = React.useState(`/api/posts/?page=${startPage}`)

  React.useEffect(() => {
    setLoading(true)
    setError(null) 
    fetch(url, { credentials: "include" }) 
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`)
        return res.json()
      })
      .then((data) => {
        setNext(data.next)
        setPrevious(data.previous)
        setCount(data.count)
        setPosts(data.results || []) 
      })
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false))
  }, [url])

  
  React.useEffect(() => {
    const p = Number(searchParams.get("page")) || 1
    if (p !== currentPage) {
      setCurrentPage(p)
      setUrl(`/api/posts/?page=${p}`)
    }
  }, [searchParams])

  function updateUrl(newApiUrl) {
    const drfUrl = new URL(newApiUrl, window.location.origin)
    const page = Number(drfUrl.searchParams.get("page")) || 1 
    setSearchParams({ page: String(page) }) 
    setUrl(`/api/posts/?page=${page}`) 
  }

  const all_posts = posts.map((post) => (
    <div key={post.id || post.slug}>
      <Link to={`/posts/${post.slug}`}><h1>{post.title}</h1></Link>
      <h2>{post.body}</h2>
      <h3>{post.author}</h3>
    </div>
  ))

  if (isLoading) return <div>loading...</div>
  if (error) return <div>{error}</div>

  const totalPages = Math.max(1, Math.ceil(count / PAGE_SIZE)) 

  return (
    <div>
      {all_posts}
      <div>
        {previous && <button onClick={() => updateUrl(previous)}>Previous</button>}
        <span> page {currentPage} of {totalPages} </span>
        {next && <button onClick={() => updateUrl(next)}>Next</button>}
      </div>
    </div>
  )
}
