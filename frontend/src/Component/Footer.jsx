import React from "react"


export default function Footer(){
    return (
        <footer className="bg-gray-800 text-gray-200 text-center py-4">
            <p>&copy; {new Date().getFullYear()} My Website. All rights reserved.</p>
        </footer>
   
    )
}