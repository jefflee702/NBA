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
    titlePanel("NBA Player Draft Position Predictor"),

    # Enter average points
    sliderInput("avg_pts", label = h3("Enter average points"), min = 1,
                max = 60, value = 1),
    
    # Enter average rebounds
    sliderInput("avg_reb", label = h3("Enter average rebounds"), min = 1,
                max = 30, value = 1),
    
    # Enter average assists
    sliderInput("avg_ast", label = h3("Enter average assists"), min = 1,
                max = 30, value = 1),
    
    # Enter player height (inches)
    sliderInput("height", label = h3("Enter player height (inches)"), 
                min = 48, max = 96, value = 48),
    
    # Enter player age (years)
    sliderInput("age", label = h3("Enter player age (years)"), 
                min = 18, max = 50, value = 18),
    
    # Enter player weight (pounds)
    sliderInput("weight", label = h3("Enter player weight (pounds)"), 
                min = 80, max = 300, value = 80),
    
    # Enter player games played
    sliderInput("gp", label = h3("Enter player games played"), 
                min = 0, max = 82, value = 0),
    
    # Enter player net rating
    sliderInput("net_rating", label = h3("Enter player net rating"), 
                min = -20, max = 20, value = -20),
    
    # Enter player offensive rebound percentage
    sliderInput("oreb_pct", label = h3("Enter player offensive rebound percentage"), 
                min = 0, max = 0.20, value = 0),
    
    # Enter player defensive rebound percentage
    sliderInput("dreb_pct", label = h3("Enter player defensive rebound percentage"), 
                min = 0, max = 0.30, value = 0), 
    
    # Enter player usage percentage
    sliderInput("usg_pct", label = h3("Enter player usage percentage"), 
                min = 0, max = 0.40, value = 0),
    
    # Enter player true shooting percentage
    sliderInput("ts_pct", label = h3("Enter player true shooting percentage"), 
                min = 0.30, max = 0.90, value = 0),
    
    # Enter player assist percentage
    sliderInput("ast_pct", label = h3("Enter player assist percentage"), 
                min = 0, max = 0.60, value = 0),
    
    # Submit button for app
    submitButton(text = "Apply", icon = NULL, width = NULL),
    
    mainPanel(
        textOutput("avg_pts"), textOutput("avg_reb"), textOutput("avg_ast"),
        textOutput("height"), textOutput("age"), textOutput("weight"), 
        textOutput("gp"), textOutput("net_rating"), textOutput("oreb_pct"),
        textOutput("dreb_pct"), textOutput("usg_pct"),
        textOutput("ts_pct"), textOutput("ast_pct"),
        textOutput("draft_position_prediction")
    )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
    
    # display predicted draft round prediction
    output$draft_position_prediction <- renderText({ 
        paste("A player with the above NBA statistics is predicted by our model to be drafted No. ",
              round(draftnum(data.frame(pts = input$avg_pts,
                                  reb = input$avg_reb,
                                  ast = input$avg_ast,
                                  player_height = input$height,
                                  age = input$age,
                                  player_weight = input$weight,
                                  gp = input$gp,
                                  net_rating = input$net_rating,
                                  oreb_pct = input$oreb_pct,
                                  dreb_pct = input$dreb_pct,
                                  usg_pct = input$usg_pct,
                                  ts_pct = input$ts_pct,
                                  ast_pct = input$ast_pct, 0)
                                  )), " overall in the NBA draft."
    
        )
        })
    
    }

# Run the application 
shinyApp(ui = ui, server = server)
