#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

source("DraftRoundPredictorFunction.R")
library(shiny)

# Define UI for application that draws a histogram
ui <- fluidPage(

    # Application title
    titlePanel("NBA Player Draft Round Predictor"),

    # Enter average points
    numericInput("av_pts", label = h3("Enter average points"), value = 0),
    
    # Enter average rebounds
    numericInput("av_reb", label = h3("Enter average rebounds"), value = 0),
    
    # Enter average assists
    numericInput("av_ast", label = h3("Enter average assists"), value = 0),
    
    mainPanel(
        textOutput("av_pts"), textOutput("av_reb"), textOutput("avg_ast"), textOutput("draft_round_prediction")
    )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
    
    # display predicted draft round prediction
    output$draft_round_prediction <- renderText({ 
        paste("A player that scores an average of ", input$av_pts, " points, recovers ", input$av_reb, 
              "rebounds, and gets ", input$av_ast, 
              "assists is predicted by the model to be drafted No. ", 
              draftnum(df = data.frame(pts = input$av_pts, reb = input$av_reb, ast = input$av_ast)), 
              "overall in an NBA draft on average.")
    })
    
    }

# Run the application 
shinyApp(ui = ui, server = server)
