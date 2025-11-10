import React from "react"

export default function() {
    const[form, setForm] = React.useState({title:"",body:""})
    
        
    

    function handleChange(e){
        const {name, value} = e.target
        setForm( formData =>{
            return {
                ...formData,
                 [name] : value
            }

        })
    }

    function handleSubmit(e){
        e.preventDefault()
        fetch("/api/posts",{
            method:"POST",
            headers:{"Content-Type": "application/json"},
            body:JSON.stringify(form)
        })
        .then(res => res.json())
        .then(data=> console.log(data))
    }

    return(
      <form onSubmit={handleSubmit}>
        <input 
         value={form.title}
         onChange={handleChange}
         placeholder="Title"
         name="title"
         type="text" />
         <textarea
           
            value={form.body}
            onChange={handleChange}
            placeholder="body"
            name="body"
           />
           <button type="submit">Create</button>
      </form>
    )
}