const article = () => {
    return(
        <Card>
            <Card.Body>
                <Card.Title>Title</Card.Title>
                <Link to={'book/' + id} className = "btn btn-primary">
                    상세보기
                </Link>
            </Card.Body>
        </Card>
    )
}

export default article 