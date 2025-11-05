import  React from "react"
import { BrowserRouter, Routes,Route, Link  } from "react-router-dom"
import Layout from "./Component/Layout"
import All_Posts from "./All_Posts"
import PostDetail from "./PostDetail"



export default function App() {


 

  return (
    <BrowserRouter>
    <Routes>

    <Route path="/" element={<Layout />}> 
     <Route index element={<All_Posts />} /> 
     <Route path="/posts/:slug" element={<PostDetail />}/>
     </Route >
  
     </Routes>
    </BrowserRouter>
  )
}



