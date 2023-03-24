#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

source("functions/DraftRoundPredictorFunction.R")
library(shiny)

# Define UI for application that draws a histogram
ui <- fluidPage(

    # Application title
    titlePanel("NBA Player Points, Assists, and Rebounds Predictor"),

    # Enter player draft position
    # numericInput("draft_pos", label = h3("Enter average points"), value = 1),
    
    sliderInput("draft_pos", label = h3("Enter player draft position"), min = 1,
                max = 60, value = 1),
    
    # Submit button for app
    submitButton(text = "Apply", icon = NULL, width = NULL),
    
    mainPanel(
        textOutput("draft_pos"),textOutput("pts_reb_ast_prediction")
    )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
    
    # display predicted draft round prediction
    output$pts_reb_ast_prediction <- renderText({ 
        paste("A player drafted No. ", input$draft_pos, " is predicted by our model to score an average of ",
               player_pred_pts(input$draft_pos), " points per game, record an average of ", 
              player_pred_ast(input$draft_pos), "assists per game, and record an average of ", 
              player_pred_reb(input$draft_pos), " rebounds per game."
    
        )
        })
    
    }

# Run the application 
shinyApp(ui = ui, server = server)
