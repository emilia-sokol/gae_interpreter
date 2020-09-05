 mapper <- function(num) {
    resultList <- list()
    if((num %% 2) == 0) {
        resultList[[ "even" ]] <- num
    } else {
        resultList[[ "odd" ]] <- num
    }
    result <- resultList
 }