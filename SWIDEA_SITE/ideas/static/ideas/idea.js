function getCSRFToken() {
    return document.querySelector('meta[name="csrf-token"]').content;
}

function toggleStar(ideaId) {
    fetch(`${ideaId}/toggle_star/`, {  // ✅ 슬래시(/) 없이 상대 경로!
        method: 'POST',
        headers: {
            'X-CSRFToken': getCSRFToken(),
        },
    })
    .then(res => res.json())
    .then(data => {
        const starIcon = document.querySelector(`.star-icon[data-id="${ideaId}"]`);
        if (data.starred) {
            starIcon.innerText = '★';
            starIcon.style.color = 'gold';
        } else {
            starIcon.innerText = '☆';
            starIcon.style.color = '#999';
        }
    });
}
function adjustInterest(ideaId, direction) {
    fetch(`${ideaId}/adjust_interest/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCSRFToken(),
        },
        body: `action=${direction}`
    })
    .then(res => res.json())
    .then(data => {
        // 해당 아이디어 카드에서 관심도 숫자만 업데이트
        const card = document.querySelector(`.idea-card button[onclick="adjustInterest(${ideaId}, '${direction}')"]`).closest('.idea-card');
        const interestText = card.querySelector('.interest-value');
        interestText.innerText = data.interest;
    });
}

window.adjustInterest = adjustInterest;