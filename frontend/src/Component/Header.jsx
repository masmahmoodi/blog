import React from "react"
import { Link } from "react-router-dom"
export default function(){
    return(
     <header className="bg-blue-600 text-white py-4 shadow-md">
        <div className="container mx-auto flex justify-between items-center px-4">
          <h1 className="text-xl font-bold">My Website</h1>
          <nav className="space-x-4">
            <Link to="/" className="hover:text-blue-200">Home</Link>
            <Link to="/about" className="hover:text-blue-200">About</Link>
            <Link to="/contact" className="hover:text-blue-200">Contact</Link>
          </nav>
        </div>
      </header>
    )
}



