import  React from "react"
import { BrowserRouter, Routes,Route, Link  } from "react-router-dom"
import Layout from "./Component/Layout"
import All_Posts from "./All_Posts"
import PostDetail from "./PostDetail"
import Edit_Post from "./Component/Edit_Post"
import Delete from "./Component/Delete"

export default function App() {


 

  return (
    <BrowserRouter>
    <Routes>

    <Route path="/" element={<Layout />}> 
     <Route index element={<All_Posts />} /> 
    <Route to="post">
     <Route path=":slug" element={<PostDetail />} />
     <Route to=":slug/edit"  element={<Edit_Post /> }/>
     <Route to="new" element={<Create_Post />} />
    </Route>
     </Route >
  
     </Routes>
    </BrowserRouter>
  )
}



